# PaperTrail!

This project aims to create a powerful, user-friendly tool that helps individuals track and analyze their spending habits. By leveraging advanced technologies like image recognition and AI parsing, this application transforms receipt data into actionable financial insights.

## Key Features

- **Receipt Analysis**

   - Upload pictures of your purchases or receipts.
   - Extract relevant details such as date, total amount, and itemized list.

- **AI Integration**

   - Integrates GPT4All to enhance parsing and provide meaningful insights from the extracted data.
   - Identifies spending patterns and suggests budgeting improvements.


## Technology Stack

- **Frontend**: HTML & CSS.
- **Backend**: Python (with Flask for deployment).
- **Machine Learning**: OpenCV for image recognition and GPT4All for AI parsing.
- **Database**: PostgreSQL for data storage & AWS S3 for image storage.

## How It Works

1. **Upload Receipts**: Users can upload images of receipts directly through the application.
2. **Data Extraction**: Using OpenCV, the system extracts text and relevant information from the receipt images.
3. **Parsing with AI**: GPT4All parses the extracted text to classify and analyze expenses.
4. **Storage:** The images are forwarded to an Amazon S3 storage bucket, and the contents of the receipt are stored in a PostgreSQL database, tied to specific users.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/budgeting-app.git
   cd budgeting-app
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python app.py
   ```

## Future Enhancements

- Mobile application for on-the-go budgeting.
- Integration with bank APIs for real-time expense tracking.
- Multi-currency support.
- Cloud-based data storage and user authentication.
- AWS SES and Lambda Function/Message Queues for storage

## Contributing

Contributions are welcome! If you’d like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to your fork.
4. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

