# import the multi_page class and the page modules
from app_pages.dashboard import dashboard_body
from app_pages.findings import findings_body
from app_pages.multi_page import MultiPage
from app_pages.summary import summary_body

# Create the app
app = MultiPage("Thames Valley Crime Insights")

# Add the pages to the app
app.add_page("Project Summary", summary_body)
app.add_page("Crime Dashboard", dashboard_body)
app.add_page("Key Findings", findings_body)

# Run the app
app.run()