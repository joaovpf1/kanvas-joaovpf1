from rest_framework import serializers
from accounts.models import Account
from contents.serializers import ContentSerializer
from courses.models import Course
from rest_framework.validators import UniqueValidator

from students_courses.serializers import StudentCourseSerializer


class CourseSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = (
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "students_courses",
            "contents",
        )
        extra_kwargs = {
            "students_courses": {"source": "students"},
            "name": {
                "validators": [
                    UniqueValidator(
                        queryset=Course.objects.all(),
                        message="course with this name already exists.",
                    )
                ]
            },
        }


class CourseStudentAddSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseSerializer(many=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "students_courses",
        ]
        extra_kwargs = {"name": {"read_only": True}}

    def update(self, instance: Course, validated_data: dict):
        students = []
        students_not_found = []
        for student_data in validated_data["students_courses"]:
            student = student_data["student"]
            student_found = Account.objects.filter(email=student["email"]).first()
            if not student_found:
                students_not_found.append(student["email"])
            else:
                students.append(student_found)
        if len(students_not_found):
            message = ", ".join(students_not_found)
            raise serializers.ValidationError(
                {"detail": f"No active accounts was found: {message}."}
            )
        instance.students.add(*students)
        return instance
