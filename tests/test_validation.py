import pytest
from app.outils.validation import email_valide


def test_email_valide_normal():
    assert email_valide("maltaarianne6@mail.fr") is True


def test_email_valide_limite_sans_arobase():
    assert email_valide("maltaarianne6mail.fr") is False


def test_email_valide_erreur_vide():
    with pytest.raises(ValueError):
        email_valide("")