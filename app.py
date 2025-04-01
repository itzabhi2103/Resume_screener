import streamlit as st
import nltk
import re
import pickle

nltk.download('punkt')
nltk.download('stopwords')

# loading models
clf = pickle.load(open('clf.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))


def cleanResume(txt):
    cleanTxt = re.sub('http\S+\s', '', txt)
    cleanTxt = re.sub('#\S+', '', cleanTxt)
    cleanTxt = re.sub('@\S+', '', cleanTxt)
    cleanTxt = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanTxt)
    cleanTxt = re.sub(r'[^\x00-\x7f]', ' ', cleanTxt)
    cleanTxt = re.sub('\s+', ' ', cleanTxt)
    return cleanTxt

# web app
def main():
    st.title('Resume Screening App')
    uploaded_file = st.file_uploader('Upload Resume', type=['txt', 'pdf'])

    if uploaded_file is not None:
        try:
            resume_bytes = uploaded_file.read()
            resume_text = resume_bytes.decode('utf-8')
        except UnicodeDecodeError:
            resume_text = resume_bytes.decode('latin-1')

        cleaned_resume = cleanResume(resume_text)
        input_features = tfidf.transform([cleaned_resume])
        prediction_id = clf.predict(input_features)[0]
        # st.write(prediction_id)

        category_mapping = {
            15: "Java Developer",
            23: 'Testing',
            8: "DevOps Engineer",
            20: "Python Developer",
            12: "HR",
            6: "Data Science",
            18: "Operations Manager",
            19: "PMO",
            3: "Blockchain",
            1: "Arts",
            7: "Database",
            0: 'Advocate',
            24: 'Web Designing',
            16: 'Mechanical Engineer',
            22: 'Sales',
            14: 'Health and fitness',
            5: 'Civil Engineer',
            4: 'Business Analyst',
            21: 'SAP Developer',
            2: 'Automation Testing',
            11: 'Electrical Engineering',
            17: 'Network Security Engineer',
            10: 'ETL Developer',
            9: 'DotNet Developer',
            13: 'Headoop'
        }

        category_name = category_mapping.get(prediction_id, "Unknown")
        st.write("Prediction Category:", category_name)

        

# python main
if __name__ == '__main__':
    main()


