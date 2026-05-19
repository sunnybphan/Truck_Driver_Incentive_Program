import pytest
from django.contrib.auth.models import User
from app.models import Profile, Organization


@pytest.fixture(scope="session")
def test_data(django_db_setup, django_db_blocker):
    """
    Create all shared test data ONCE per test session.
    """
    with django_db_blocker.unblock():
        org = Organization.objects.create(name="Sponsor A")

        user = User.objects.create_user(username="davethedriver", password="123")
        profile, _ = Profile.objects.get_or_create(user=user)

        profile.organizations.add(org)

        return {
            "user": user,
            "profile": profile,
            "org": org,
        }
