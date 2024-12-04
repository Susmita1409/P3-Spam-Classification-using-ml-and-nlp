import streamlit as st
import pickle
model = pickle.load(open('spm123.pkl','rb'))
cv = pickle.load(open('vec123.pkl','rb'))

def main():
  st.title("Email Spam Classification Aplication")
  st.write("This is a Machine Learning application to classify")
  st.subheader("Classifiction")
  user_input=st.text_area("Enter an email to classify",height=150)
  if st.button("Clssify"):
    if user_input:
      data=[user_input]
      print(data)
      vec=cv.transform(data).toarray()
      result=model.predict(vec)
      if result[0]==0:
        st.success("This is not a spam email")
      else:
         st.error("This is a spam email")
  else:
    st.write("please enter an email to classify")
main()
        