# 📄 AI-Powered Resume Screening Tool  

**Automatically classify resumes into roles like *Python Developer*, *Machine Learning Engineer*, or *Data Scientist* using NLP.**  

![Demo](assets/demo.gif) *(Optional: Add a GIF/screenshot of your Streamlit app)*  

## 🚀 Features  
- **Role Prediction**: Classifies resumes into tech roles (Python, ML, Data Science, etc.).  
- **NLP Processing**: Uses **TF-IDF, NLTK, and Regex** to extract and analyze skills.  
- **User-Friendly UI**: Built with **Streamlit** for easy uploads and predictions.  
- **Scalable**: Can be extended to more job categories.  

## 🛠️ Tech Stack  
- **Python** (NLP Libraries: `nltk`, `re`, `scikit-learn`)  
- **TF-IDF Vectorization** (Text feature extraction)  
- **Streamlit** (Web framework)  
- **Kaggle Datasets** (Training data)  

## 📦 Installation  
1. **Clone the repo**:  
   ```bash  
   git clone https://github.com/yourusername/resume-screening.git  
   cd resume-screening
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   
3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
##🧠 How It Works
- Upload a resume (PDF or text).
- The model cleans text (removes stopwords, punctuation) and extracts features using TF-IDF.
- Predicts the role based on trained data (e.g., "Python Developer" or "Data Scientist").
