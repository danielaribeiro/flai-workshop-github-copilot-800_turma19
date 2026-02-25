from django.core.management.base import BaseCommand
from django.db import transaction

from octofit_tracker.models import Team, UserProfile, Activity, LeaderboardEntry, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        with transaction.atomic():
            # Clear existing data
            LeaderboardEntry.objects.all().delete()
            Activity.objects.all().delete()
            Workout.objects.all().delete()
            UserProfile.objects.all().delete()
            Team.objects.all().delete()

            # Create teams
            marvel = Team.objects.create(name='marvel')
            dc = Team.objects.create(name='dc')

            # Sample superhero users
            heroes = [
                ('Tony Stark', 'tony@stark.com', marvel),
                ('Steve Rogers', 'steve@avengers.com', marvel),
                ('Peter Parker', 'peter@spider.com', marvel),
                ('Bruce Wayne', 'bruce@wayne.com', dc),
                ('Clark Kent', 'clark@krypton.com', dc),
                ('Diana Prince', 'diana@themyscira.com', dc),
            ]

            for name, email, team in heroes:
                user = UserProfile.objects.create(name=name, email=email, team=team)
                Workout.objects.create(name=f"{name} Workout", description='Sample workout', created_by=user)
                Activity.objects.create(user=user, activity_type='running', duration_minutes=30, distance_km=5.0)
                LeaderboardEntry.objects.create(user=user, points=100)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with sample data'))
