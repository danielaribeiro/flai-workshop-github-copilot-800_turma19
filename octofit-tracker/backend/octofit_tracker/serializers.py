from rest_framework import serializers
from .models import Team, UserProfile, Activity, LeaderboardEntry, Workout


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']


class UserProfileSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    team_id = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), source='team', write_only=True, required=False, allow_null=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'email', 'team', 'team_id']


class ActivitySerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), source='user', write_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_id', 'activity_type', 'duration_minutes', 'distance_km', 'timestamp']


class LeaderboardEntrySerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), source='user', write_only=True)

    class Meta:
        model = LeaderboardEntry
        fields = ['id', 'user', 'user_id', 'points', 'rank']


class WorkoutSerializer(serializers.ModelSerializer):
    created_by = UserProfileSerializer(read_only=True)
    created_by_id = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), source='created_by', write_only=True, required=False, allow_null=True)

    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'difficulty', 'created_by', 'created_by_id']
