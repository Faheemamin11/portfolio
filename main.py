import streamlit as st
import base64
from datetime import datetime
from PIL import Image  # For handling images if you add them

# Set page config - this must be the first Streamlit command
st.set_page_config(
    page_title="My Portfolio",
    page_icon="👨‍💻",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
def load_css():
    st.markdown("""
    <style>
        /* Main content */
        .main {
            max-width: 1000px;
            padding: 2rem;
        }
        
        /* Project cards */
        .project-card {
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.1);
            margin-bottom: 30px;
            transition: box-shadow 0.3s;
        }
        .project-card:hover {
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
        }
        
        /* Technology tags */
        .tech-pill {
            display: inline-block;
            padding: 5px 10px;
            background-color: #f0f2f6;
            border-radius: 20px;
            margin: 5px 5px 5px 0;
            font-size: 0.8em;
        }
        
        /* PDF viewer container */
        .pdf-container {
            display: flex;
            justify-content: center;
            margin: 20px 0;
        }
        
        /* Download button */
        .download-btn {
            width: 100%;
            margin-top: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

# Load CSS
load_css()

# Sidebar navigation and info
def sidebar():
    with st.sidebar:
        st.title("Navigation")
        page = st.radio("Go to", 
                       ("Resume", "Projects 1", "Projects 2"),
                       label_visibility="collapsed")
        
        st.markdown("---")
        st.header("Contact Info")
        st.markdown("📧 Fahimamin017@gmail.com")
        st.markdown("📱 +92 323 8608816")
        st.markdown("💼 [LinkedIn](https://www.linkedin.com/in/faheem-amin-44988a1a7/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)")
        st.markdown("🐙 [GitHub](https://github.com/Faheemamin11)")
        
        st.markdown("---")
        st.write(f"© {datetime.now().year} Faheem Amin. All rights reserved.")
    
    return page

# Resume page
def resume_page():
    st.title("My Professional Resume")
    st.markdown("---")
    
    # Header with basic info
    col1, col2 = st.columns([3, 1])
    with col1:
        st.header("Hafiz Muhammad Faheem Amin")
        st.subheader("Data Analyst | Administrative")
        st.write("""
        Results-driven professional with 3+ years in Administration, IT management, and operations, now transitioning into data analytics with expertise in Python, pandas, visualization, and dashboard creation..
        """)
    
    with col2:
        # Add your photo if you want (uncomment and add image to assets folder)
        # st.image("assets/profile.jpg", width=150)
        pass
    
    st.markdown("---")
    
    # PDF Viewer Function
    def show_pdf(file_path):
        try:
            with open(file_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f"""
            <div class="pdf-container">
                <iframe src="data:application/pdf;base64,{base64_pdf}" 
                        width="1200" 
                        height="1000" 
                        style="border: none;">
                </iframe>
            </div>
            """
            st.markdown(pdf_display, unsafe_allow_html=True)
        except FileNotFoundError:
            st.error("Resume PDF not found. Please ensure 'resume.pdf' is in the folder.")
    
    # Display PDF
    show_pdf("Faheem Amin CV.pdf")
    
    # Download button
    try:
        with open("Faheem Amin CV.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name="YourName_Resume.pdf",
            mime="application/octet-stream",
            use_container_width=True
        )
    except:
        st.warning("Could not load download button. PDF file missing.")

# Projects Page 1
def projects_page_2():
    st.title("Pharmaceutical Usage Dashboard")
    st.markdown("""
    A Streamlit application analyzing prescription patterns for 8 key medications.
    """)

    with st.container():
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        
        

        st.image("pharma.png", caption="Dashboard Overview")

        st.header("Medication Usage Analysis")
        st.markdown("""
        An interactive dashboard tracking prescription patterns for 8 key medications.
        """)
        
        
        
        st.markdown("""
        **What I Built:**
        - Cleaned and analyzed prescription data for 8 medications
        - Created interactive time-series charts of daily usage
        - Developed weekday analysis to see prescription patterns
        - Added filters by date ranges and specific medications
        - Designed correlation analysis between medications
        
        **Technical Work:**
        - Processed raw CSV data from Kaggle
        - Extracted day/month/year from dates for analysis
        - Built multi-select filters for medications
        - Created responsive visualizations
        - Deployed on Streamlit Cloud
        """)
        
        st.markdown("""
        **Project Links:**  
        [GitHub Code](https://github.com/Faheemamin11/pharma_dashboard) | 
        [Live Dashboard](https://pharmadashboard.streamlit.app/) | 
        [Dataset Source](https://www.kaggle.com/code/milanzdravkovic/pharma-sales-data-analysis-and-forecasting/input)
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
   
# Projects Page 2
def projects_page_1():
    
    st.title("Superstore Analytics Dashboard")
    st.header("📊 Superstore Analytics: Interactive Business Intelligence Platform")
    
    tab1, tab2, tab3 = st.tabs(["Overview", "Key Features", "Technical Implementation"])
    
    with tab1:
        st.markdown("""
        A comprehensive data analytics dashboard built to transform raw Superstore sales data 
        into actionable business insights through interactive visualizations and advanced analytics.
        """)
        
        # Replace with actual screenshot of your dashboard
        st.image("superstore.png", caption="Dashboard Overview")
        # st.markdown("![Dashboard Screenshot](https://via.placeholder.com/800x400?text=Superstore+Analytics+Dashboard)")
        
        st.markdown("""
        **Business Value:**
        - Enables data-driven decision making for retail operations
        - Identifies sales trends and profit opportunities
        - Tracks performance across regions and product categories
        - Provides executive-level KPI monitoring
        """)
            
    with tab2:
        st.markdown("""
        **Core Functionalities:**
        - Interactive filtering by region, category, date range, and customer segment
        - Sales and profit trend analysis with time-series visualizations
        - Geographical heatmaps showing regional performance
        - Top N analysis for products, states, and cities
        - Sales representative performance tracking
        - Automated notification system (SMS/Email) for key metrics
        - Responsive design for desktop and mobile viewing
        """)
        
        st.markdown("""
        **Data Insights Provided:**
        - Identify highest performing products/categories
        - Detect seasonal sales patterns
        - Pinpoint most profitable customer segments
        - Visualize geographical sales distribution
        - Monitor discount impact on profitability
        """)
            
    with tab3:
        st.markdown("""
        **Technical Architecture:**
        - Frontend: Streamlit for interactive web interface
        - Visualization: Plotly for dynamic charts and maps
        - Data Processing: Pandas for ETL and calculations
        - Notification Services:
          - Twilio API for SMS alerts
          - SMTP for email notifications
        - Performance Optimization:
          - Caching with @st.cache_data
          - Lazy loading of visualizations
        """)
        
        st.markdown("""
        **Development Tools:**
        - Python 3.9+
        - VS Code with Jupyter extension
        - Git/GitHub for version control
        - Streamlit Cloud for deployment
        - Plotly Express for rapid charting
        """)
    
    st.markdown("""
    **Project Links:**  
    [GitHub Repository](https://github.com/Faheemamin11/superstore_analysis) | 
    [Live Demo](https://faheemamin.streamlit.app/) | 
    [Dataset Source](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
    """)
    
    st.markdown("""
    **Future Enhancements:**
    - Predictive analytics with Profit
    - Customer segmentation with clustering
    - Automated report generation
    - Integration with live data sources
    """)
    

# Main app logic
def main():
    page = sidebar()
    
    if page == "Resume":
        resume_page()
    elif page == "Projects 1":
        projects_page_1()
    elif page == "Projects 2":
        projects_page_2()

if __name__ == "__main__":
    main()