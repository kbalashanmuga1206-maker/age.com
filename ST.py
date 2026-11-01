import streamlit as st
from datetime import date

st.set_page_config(page_title="Age Calculator", page_icon="🎂")

st.title("🎂 Age Calculator")

today = date.today()

birth_date = st.date_input(
    "Enter your Date of Birth",
    value=date(2005, 1, 1),
    min_value=date(1900, 1, 1),
    max_value=today,
    format="DD-MM-YYYY",
)


def birthday_in_year(year):
    """Return the birthday for a given year (Feb 29 -> Feb 28 in non-leap years)."""
    try:
        return date(year, birth_date.month, birth_date.day)
    except ValueError:
        return date(year, 2, 28)


if st.button("Calculate"):
    # Calculate age
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    # Calculate next birthday
    next_birthday = birthday_in_year(today.year)
    if next_birthday < today:
        next_birthday = birthday_in_year(today.year + 1)

    days_left = (next_birthday - today).days

    st.subheader("Your Details")
    col1, col2 = st.columns(2)
    col1.metric("Your Age", f"{age} years")
    col2.metric("Days Until Birthday", days_left)

    st.write(f"**Date of Birth:** {birth_date.strftime('%d-%m-%Y')}")
    st.write(f"**Current Date:** {today.strftime('%d-%m-%Y')}")
    st.write(f"**Next Birthday:** {next_birthday.strftime('%d-%m-%Y')}")

    if days_left == 0:
        st.balloons()
        st.success("Happy Birthday! 🎉")
