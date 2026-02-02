import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game", page_icon="🎲")

def main():
    st.title("NUMBER GUESSING GAME")
    st.write("Welcome to the Number Guessing Game! Try to guess the number I'm thinking of between 1 and 100.")
    st.write("You have 10 attempts to guess the correct number.")

    if "number_to_guess" not in st.session_state:
        st.session_state.number_to_guess = random.randint(1, 100)
        st.session_state.attempts = 10
        st.session_state.score = 10

    user_input = st.text_input("Enter your guess (0-100):")

    if st.button("Submit Guess"):
        try:
            user_guess = int(user_input)
            if not (0 <= user_guess <= 100):
                st.error("Please enter a number between 0 and 100.")
                return
        except ValueError:
            st.error("Please enter a valid integer.")
            return

        if st.session_state.attempts > 0:
            if user_guess < st.session_state.number_to_guess:
                st.warning("Too low! Try again.")
                st.session_state.score -= 1
                st.warning(f"Your score is now: {st.session_state.score} points.")
            elif user_guess > st.session_state.number_to_guess:
                st.warning("Too high! Try again.")
                st.session_state.score -= 1
                st.warning(f"Your score is now: {st.session_state.score} points.")
            else:
                st.success("Congratulations! You've guessed the correct number!")
                st.success(f"Your final score is: {st.session_state.score} points.")
                return
            st.session_state.attempts -= 1
            st.info(f"You have {st.session_state.attempts} attempts left.")
        else:
            st.error(f"Game over! The correct number was {st.session_state.number_to_guess}.")

    if st.button("Restart Game"):
        st.session_state.number_to_guess = random.randint(1, 100)
        st.session_state.attempts = 10
        st.session_state.score = 10

if __name__ == "__main__":
    main()