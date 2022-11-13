import jamspell

def correct_text(text):
    corrector = jamspell.TSpellCorrector()
    corrector.LoadLangModel('en.bin')
    return corrector.FixFragment(text)
