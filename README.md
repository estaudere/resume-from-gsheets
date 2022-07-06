# resume-from-gsheets

This app will allow you to create a resume from a properly formatted Google Sheet. Once 
you've created your Google Sheet with information, you can download your finished resume 
as a PDF.

To use, create a Google Sheet by copying [this template](https://docs.google.com/spreadsheets/d/1GBRTwNO_GSldGLUBWlBlUB9W-y3S8sE2x023My2vagw/) and replacing the template information.

This app is built in Flask and uses `weasyprint` to convert HTML and CSS to a styled PDF.

## Running locally

Ensure that you've installed `flask`, `weasyprint`, `flask-weasyprint`, and `requests`,
and follow the instructions for the [Google API Console](https://developers.google.com/sheets/api/guides/authorizing) 
to obstain an API key (0Auth is not needed). Then create a `.env` file with the following 
information:

```text
G_KEY=<APIKEY>
```

You should be able to run `python app.py` in start your server.