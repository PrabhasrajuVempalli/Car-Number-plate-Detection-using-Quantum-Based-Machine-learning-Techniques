# Setup Instructions

## Prerequisites
- Python 3.8+
- [Git](https://git-scm.com/)
- Appropriate GPU drivers (optional, for YOLO acceleration)

## Installation Steps
1. **Clone the repository**:
   ```bash
   git clone [Your Repository Link]
   cd ampr
   ```

2. **Create a virtual environment (Recommended)**:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python -m streamlit run src/app.py
   ```
   
Open the resulting local URL in your web browser to view the application dashboard.
