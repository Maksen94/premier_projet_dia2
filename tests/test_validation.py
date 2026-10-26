import pytest
from app.outils.validation import email_valide, mdp_robuste, code_postal


def test_email_valide_normal():
    assert email_valide("maltaarianne6@mail.fr") is True


def test_email_valide_limite_sans_arobase():
    assert email_valide("maltaarianne6mail.fr") is False


def test_email_valide_erreur_vide():
    with pytest.raises(ValueError):
        email_valide("")




def test_mdp_robuste_normal():
    assert mdp_robuste("Abcdef1!") is True


def test_mdp_robuste_limite_7_caracteres():
    assert mdp_robuste("Abcde1!") is False


def test_mdp_robuste_faible_sans_special():
    assert mdp_robuste("abcdefgh") is False


def test_mdp_robuste_erreur_vide():
    with pytest.raises(ValueError):
        mdp_robuste("")




def test_code_postal_normal():
    assert code_postal("94000") is True


def test_code_postal_limite_4_chiffres():
    assert code_postal("9400") is False


def test_code_postal_lettres():
    assert code_postal("94A00") is False


def test_code_postal_erreur_vide():
    with pytest.raises(ValueError):
        code_postal("")