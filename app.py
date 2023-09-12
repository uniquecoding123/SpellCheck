from textblob import TextBlob
from spellchecker import SpellChecker
import streamlit as st

st.title("Spell/Grammer check")
text = st.text_area("Enter your text here:")
file = st.file_uploader("you can Upload a file here", type=["txt", "csv", "xlsx"])

blob = TextBlob(text)

corrected_text = blob.correct()

def mistake_words(sent):
    spell = SpellChecker()
    words = sent.split()
    misspelled = spell.unknown(words)
    mistakes = list(misspelled)
    st.success("The corrected text is...\t\t\t"+str(corrected_text))
    st.warning('The number of mistake/mistakes....  ' + str(len(mistakes)))
    st.write('The mistakes are....   ' + str(list(mistakes)))


def mistake_flie(file):
    spell = SpellChecker()
    words = file.split()
    misspelled = spell.unknown(words)
    mistakes = list(misspelled)
    st.write("The corrected text is...  "+str(corrected_text))
    st.write('The number of mistake/mistakes....    ' + str(len(mistakes)))
    st.write('The mistakes are..    ' + str(list(mistakes)))


if st.button('check'):
    if text or file:
        if text:
            mistake_words(text)
        else:
            mistake_flie(text)
    else:
        st.warning("Please enter the text or Upload the file..")

# Print the misspelled words
