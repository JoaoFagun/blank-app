
# Import Python packages
import streamlit as st
# from snowflake.snowpark.context import get_active_session
from streamlit.components.v1 import html   # built-in Streamlit component
from PIL import Image  # Function to display the "About" page


# 1) Tell browsers where the manifest lives
st.markdown(
    '<link rel="manifest" href="static/manifest.json">',
    unsafe_allow_html=True
)

# 2) (Optional) register your service worker
st.markdown(
    '<script src="static/service-worker.js"></script>',
    unsafe_allow_html=True
)

def centered_title(text: str):
    st.markdown(f"<h1 style='text-align:center'>{text}</h1>", unsafe_allow_html=True)

def centered_header(text: str):
    st.markdown(f"<h2 style='text-align:center'>{text}</h2>", unsafe_allow_html=True)

def show_about():
    centered_title("About the CarbonSat Project")
    st.write("""
    CarbonSat was developed as part of the final degree project (PIC) by eight undergraduate students at Instituto Superior Técnico (University of Lisbon, Portugal),
    under the supervision of Professor Manuel Heitor and Afonso Gusmão.
    
    The project is based on a case study from the LIFE Maronesa Project in Vila Pouca de Aguiar and aims to combine academic research with practical application to address real-world
    challenges in soil monitoring and carbon management.

    CarbonSat represents a multidisciplinary effort, bringing together remote sensing, environmental sciences, and machine learning to create a tool that not only advances scientific
    understanding but also supports sustainable land use and climate action.
    """)
    try:
        prof_img = Image.open("Professores.png")
        st.image(prof_img, width=300)            
    except FileNotFoundError:
        st.error("Header image 'carbonsat.jpeg'")
    st.subheader("The LIFE Maronesa Project in Vila Pouca de Aguiar")
    st.write("""
    The LIFE Maronesa Project is an initiative for Governance, Information, and Climate Action.
    
    Its main objective is to improve the governance of community-based extensive grazing and raise awareness of the socio-environmental benefits of this method of production, based on evidence.

    The project addresses the abandonment of mountain pastures, especially on community-owned common lands, the increasing intensity of wildfires in summer, the reduction of carbon stocks
    sequestered in soil organic matter in mountainous areas, and the decline of the Maronesa cattle population.

    Its primary aim is to enhance the climate resilience of cattle farms and promote increased carbon retention in soil organic matter.
    """)
    try:
        vpa1_img = Image.open("VPA1.png")
        st.image(vpa1_img, width=700)            
    except FileNotFoundError:
        st.error("Header image 'carbonsat.jpeg'")
    
    st.subheader("Real-world Impact")
    st.write("""
    *Decision-makers:*  
    Monitor SOC (Soil Organic Carbon) sequestration trends for public policy decisions.

    *Farmers & Landowners:*  
    Monitor SOC trends to support regenerative agriculture and eligibility for carbon credits.

    *Researchers:*  
    Leverage validated SOC change data for environmental modelling and climate studies.
    """)

    st.subheader("Methodology")
    st.write("""
    The methodology employed in CarbonSat is based on combining advanced remote sensing techniques, field data collection, and machine learning models, ensuring data accuracy and reliability for environmental policy decision-making.
    """)

    # Contact
    st.subheader("Contact")
    st.write("""
    For more information, get in touch at [carbonsatist@gmail.com](mailto:carbonsatist@gmail.com)
    """)
def show_maps(category: str):
    
    centered_title("Interactive Maps and Statistics")
    
    if category == "Index Data":
        
        st.write("""
    Below are several charts and maps presenting data visualisations of vegetation indices and their spatio-temporal distribution across different regions and seasons. These charts focus mainly on various spectral indices such as NDVI, MSAVI2, NDWI, EVI2, and BSI, and represent the relationship between these indices and soil carbon dynamics.
    """)
        st.write("""
        - *Average of NDVI, NDWI, BSI, EVI2, and MSAVI2*: Average values of these indices in the seasons (Autumn, Winter, Spring) from 2018 to 2021, by plot.
        - *Temporal Variation*: The temporal variation of spectral indices (2018–2021), showing seasonal fluctuations.
                 """)
        embed_url1 = "https://app.powerbi.com/view?r=eyJrIjoiZDhkYmRiZWEtNTUzYS00ODFlLWI1ZjItNzA3MDY2ZTYwNmRjIiwidCI6IjBiZmE4NTAwLWIxZjItNDU2Ni1iYWYxLTZmNTkzNzA4OTNlNyIsImMiOjh9"

        html(
            f"""
            <iframe
                width="100%"
                height="550"
                src="{embed_url1}"
                frameborder="0"
                allowfullscreen="true"
                sandbox="allow-scripts allow-same-origin allow-forms allow-popups">
            </iframe>
            """,
            height=550,   # Streamlit reserves vertical space
        )

        embed_url2 = "https://app.powerbi.com/view?r=eyJrIjoiZDhkYmRiZWEtNTUzYS00ODFlLWI1ZjItNzA3MDY2ZTYwNmRjIiwidCI6IjBiZmE4NTAwLWIxZjItNDU2Ni1iYWYxLTZmNTkzNzA4OTNlNyIsImMiOjh9&pageName=5fc34f4870a4e0a74806"

        html(
            f"""
            <iframe
                width="100%"
                height="550"
                src="{embed_url2}"
                frameborder="0"
                allowfullscreen="true"
                sandbox="allow-scripts allow-same-origin allow-forms allow-popups">
            </iframe>
            """,
            height=550,   # Streamlit reserves vertical space
        )
        
        st.write("""
        These charts and maps help understand how spectral indices vary across seasons and between areas, providing valuable insights into soil and vegetation changes.
        """)

        st.subheader("Contact")
        st.write("""
        For more information, get in touch at [carbonsatist@gmail.com](mailto:carbonsatist@gmail.com)
        """)
    elif category == "Index Spatial distribution":
        centered_title("Index Spatial distribution")
        html(
            """
            <div style="display:flex;justify-content:center;">
                <iframe
                width="600"
                height="373.5"
                src="https://app.powerbi.com/view?r=eyJrIjoiZDhkYmRiZWEtNTUzYS00ODFlLWI1ZjItNzA3MDY2ZTYwNmRjIiwidCI6IjBiZmE4NTAwLWIxZjItNDU2Ni1iYWYxLTZmNTkzNzA4OTNlNyIsImMiOjh9"
                frameborder="0"
                allowfullscreen="true"
                </iframe>
            </div>
            """,
             height=500
        )
    else:
        st.write("Mapping spatial distribution of carbon across regions.")

def show_calibration_sensor():
    centered_title("Calibration Sensor")
    st.write("""
    To ensure that the data obtained through the Random Forest are as accurate as possible, it is essential to use a sensor capable of obtaining precise measurements. Our sensor employs Laser-induced Breakdown Spectroscopy (LIBS) technology to easily obtain accurate carbon measurements at depths of 5, 10, 15, and 20 cm.
    """)
    
    st.subheader("Sensor Specifications")
    st.write("""
    *Power Supply and Power Management:*  
    The solar panel provides energy to power the system and charge the lithium-ion battery. The TP4056 charger manages battery charging and prevents overcharging. The LM2596 buck converter steps down the battery voltage to provide stable power to the system components, ensuring energy efficiency in remote locations.
    
    *Control and Communication (ESP32):*  
    The ESP32 microcontroller manages the system, controls the LIBS sensor and stepper motor, and transmits data remotely via Wi-Fi or Bluetooth, ensuring autonomy and remote access without needing physical presence.
    
    *Measurements and Actuation (LIBS, NEMA 17 Stepper Motor):*  
    The LIBS sensor analyses soil carbon content using a laser pulse. The NEMA 17 stepper motor adjusts the sensor position at different depths, with precise control by the A4988 driver, operating at 12V.
    """)
    st.subheader("Our Prototype")
    st.write("""
             describe our prototype"""
             )
    try:
        sensor1_img = Image.open("Sensor1.jpeg")
        st.image(sensor1_img, width=300)            
    except FileNotFoundError:
        st.error("Header image 'carbonsat.jpeg'")

    st.subheader("Contact")
    st.write("""
    For more information, get in touch at [carbonsatist@gmail.com](mailto:carbonsatist@gmail.com)
    """)


def main():
    # Optional but recommended: page metadata
    st.set_page_config(page_title="CarbonSat", layout="wide")
    

# Initialize session state flag
    if 'show_sidebar' not in st.session_state:
        st.session_state.show_sidebar = False

    # Hamburger‐style button in the main area
    # You can use an emoji or any label you like
    
    try:
        header_img = Image.open("carbonsat.png")
        # Your existing two‐column layout
        col1, col2 = st.columns([1, 11])
        with col1:
            if st.button("☰", key="hamburger"):
                st.session_state.show_sidebar = not st.session_state.get("show_sidebar", False)
        with col2:
            sub1, sub2, sub3 = st.columns([1, 1, 1])
            sub2.image(header_img, width=500)  # ← adjust width in px as needed
            #centered_title("CarbonSat")
            centered_header("Welcome to CarbonSat!")
            # Nested three‐column layout inside col2 to centre the image
            
    except FileNotFoundError:
        st.error("Header image 'carbonsat.jpeg' not found. Please add it to the app directory.")

   
    
    # CSS injection for styling
    st.markdown(
        """
        <style>
            .stApp {
                background-color: rgb(46, 181, 101);
            }
            /* Dark olive sidebar background */
                [data-testid="stSidebar"] > div {
                    background-color: #10A5AC !important;
            }

            /* universal button style */
            div.stButton > button:first-child {
                width: 42px;
                max-width: 220px;
                height: 48px;
                margin: 12px auto;
                font-size: 16px;
                border: 2px solid #000;
                border-radius: 6px;
                background: #10A5AC;
                color: #fff;
                display: block;
            }
            #hamburger-container.stButton > button {
                width: 34px !important;
                height: 41px !important;
                padding: 2px !important;
                font-size: 16px !important;     /* adjust icon size if needed */
                border-radius: 4px !important;  /* optional rounding */
            }

        </style>
        """,
        unsafe_allow_html=True
    )
    # Header image as site header
    
    #centered_header('Welcome to CarbonSat!')
    st.write("""
    CarbonSat is a soil monitoring platform using sensors and satellite imagery.
    Select one of the options below to start:
    """)
    try:
        vpa1_img = Image.open("VPA1.png")
        st.image(vpa1_img, width=700)            
    except FileNotFoundError:
        st.error("Header image 'carbonsat.jpeg'")

    if st.session_state.show_sidebar:
        with st.sidebar:
            try:
                 sidebar_img = Image.open("carbonsat.jpeg")
                 st.image(sidebar_img, width=100)
                 
            except FileNotFoundError:
                st.error("Header image 'carbonsat.jpeg' not found. Please add it to the app directory.")
            
            #st.title("CarbonSat")
            st.title("Explore Us")
            choice = st.radio("Go to", ["Home", "About", "Maps", "Calibration Sensor"], key="page_sel")
            if choice == "Maps":
                st.selectbox("Category", ["Index Data", "Index Spatial Distribution", "Spatial Distribution"], key="map_category")
                st.session_state.page = 'maps'
            else:
                st.session_state.page = choice.lower().replace(" ", "_")
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    

    if st.session_state.page == 'about':
        show_about()
    elif st.session_state.page == 'calibration_sensor':
        show_calibration_sensor()
    elif st.session_state.page == 'maps':
        show_maps(st.session_state.map_category)
    else:
        st.write("Choose one of the options to navigate through the pages.")

if __name__ == "__main__":
    main()

