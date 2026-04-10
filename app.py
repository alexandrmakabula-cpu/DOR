import streamlit as st

# Настройки страницы
st.set_page_config(page_title="DOR Calculator", page_icon="🧗")

# Словари перевода
LANGS = {
    "RU": {
        "title": "DOR CALCULATOR",
        "h": "Высота (h)", "x": "Ср. пролет (x̄)", "n": "Зацепы (N)",
        "size": "Размер (size)", "k_type": "k_type", "k_tech": "k_tech", 
        "k_text": "k_text", "mult": "Множитель", "btn": "РАССЧИТАТЬ",
        "res": "ИТОГОВЫЙ РЕЙТИНГ"
    },
    "UA": {
        "title": "КАЛЬКУЛЯТОР DOR",
        "h": "Висота (h)", "x": "Сер. проліт (x̄)", "n": "Зачепи (N)",
        "size": "Розмір (size)", "k_type": "k_type", "k_tech": "k_tech", 
        "k_text": "k_text", "mult": "Множник", "btn": "РОЗРАХУВАТИ",
        "res": "ПІДСУМКОВИЙ РЕЙТИНГ"
    },
    "EN": {
        "title": "DOR CALCULATOR",
        "h": "Height (h)", "x": "Avg span (x̄)", "n": "Rocks count (N)",
        "size": "Hold size", "k_type": "k_type", "k_tech": "k_tech", 
        "k_text": "k_text", "mult": "Multiplier", "btn": "CALCULATE",
        "res": "FINAL RATING"
    }
}

# Выбор языка в сайдбаре или сверху
lang = st.radio("Language / Мова / Язык", ["RU", "UA", "EN"], horizontal=True)
t = LANGS[lang]

st.title(f"🚀 {t['title']}")
st.markdown("---")

# Создаем колонки для ввода данных
col1, col2 = st.columns(2)

with col1:
    h = st.number_input(t['h'], value=0.0, step=0.1, format="%.2f")
    x_bar = st.number_input(t['x'], value=0.0, step=0.1, format="%.2f")
    n_rocks = st.number_input(t['n'], value=0.0, step=1.0)
    size = st.number_input(t['size'], value=0.5, step=0.05, format="%.2f")

with col2:
    k_type = st.number_input(t['k_type'], value=0.3, step=0.1)
    k_tech = st.number_input(t['k_tech'], value=0.1, step=0.1)
    k_text = st.number_input(t['k_text'], value=0.1, step=0.1)
    multiplier = st.number_input(t['mult'], value=5.0, step=1.0)

st.markdown("---")

if st.button(t['btn'], use_container_width=True):
    try:
        # Формула: (h * x) / (n + 1/(2*size)) * (sum k) * multiplier
        geometry = (h * x_bar) / (n_rocks + (1 / (2 * size)))
        coeffs = k_type + k_tech + k_text
        result = geometry * coeffs * multiplier
        
        st.subheader(t['res'])
        st.code(f"{result:.4f}", language="text")
        st.balloons() # Маленький эффект праздника при расчете
    except ZeroDivisionError:
        st.error("Ошибка: Проверьте вводимые данные (size или N не могут быть 0)")
