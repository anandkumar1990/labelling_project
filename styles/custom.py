def get_custom_css():
    return """
    <style>
        /* Base styling and gradient background */
        .main {
            background: linear-gradient(135deg, #f5f7fa 0%, #e4e9f2 100%);
            min-height: 100vh;
            padding: 2rem;
        }
        
        /* Resume content area */
        .resume-content {
            background: white;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            margin-bottom: 2rem;
            font-size: 3.4rem !important;
            border: 2px solid #bbb;
        }
        .resume-content-scroll {
            max-height: 420px;
            overflow-y: auto;
            white-space: pre-wrap;
            scrollbar-width: thin;
            scrollbar-color: #888 #eee;
        }
        .resume-content-scroll::-webkit-scrollbar {
            width: 10px;
        }
        .resume-content-scroll::-webkit-scrollbar-thumb {
            background: #bbb;
            border-radius: 8px;
        }
        .resume-content-scroll::-webkit-scrollbar-track {
            background: #eee;
            border-radius: 8px;
        }
        
        /* Navigation buttons container */
        .nav-buttons {
            display: flex;
            flex-direction: column;
            gap: 1rem;
            position: sticky;
            top: 2rem;
        }
        
        /* Button styling */
        .stButton > button {
            width: 100%;
            font-size: 2.4rem !important;
            padding: 1.5rem 1rem !important;
            border-radius: 12px !important;
            margin: 0.5rem 0;
            background: #4a90e2;
            color: white;
            border: none;
            transition: all 0.3s ease;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
            background: #357abd;
        }
        
        /* File counter styling */
        .file-counter {
            font-size: 2.2rem;
            text-align: center;
            padding: 1rem;
            background: white;
            border-radius: 10px;
            margin: 1rem 0;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }
        
        /* Input fields */
        .stTextInput > div > div > input {
            font-size: 2.2rem !important;
            padding: 1.5rem;
            border-radius: 12px;
        }
        
        /* Select box */
        .stSelectbox > div > div {
            font-size: 2.2rem !important;
            padding: 1.2rem !important;
        }
        
        /* Headers */
        h1 {
            font-size: 4rem !important;
            color: #2c3e50;
            margin-bottom: 2rem;
        }
        
        h2, h3 {
            font-size: 3rem !important;
            color: #2c3e50;
        }
        
        /* Entity annotation text */
        .st-emotion-cache-1y4p8pa {
            font-size: 2.4rem !important;
            line-height: 1.6 !important;
        }
        
        /* Text content */
        .st-ae {
            font-size: 2.4rem !important;
        }
        
        .annotation-content, .annotation-text {
            font-size: 2.4rem !important;
            line-height: 1.6 !important;
        }
        
        /* Make the content area use maximum available space */
        .block-container {
            padding: 2rem !important;
            max-width: 100% !important;
        }
        
        /* Ensure text is readable in the resume content */
        .resume-content p, 
        .resume-content span, 
        .resume-content div {
            font-size: 2.4rem !important;
            line-height: 1.6 !important;
            color: #333;
        }
    </style>
    """


