import smtreamlit as st
#--------INITIAL BOOK DATABASE-------
books = [
"the hobbit",
  "1984",
  "to kill a mockingbird",
  "the great gatsby"
]
#-------APPP TITLE-------
st.title("book checker app")
st.write("enter a book title to check if it exists in the database")
#-------USER INPUT-------
uaer_input = st.text_input("book title")
#-------CHECK BUTTON-------
if st.button("check book")
if user_input.strip() == "":
  st.warning("please enter a book title")
elif user_input in books:
  st.success("the book exists in the database")
else:
  st.error("the book wasnt found in the database")
