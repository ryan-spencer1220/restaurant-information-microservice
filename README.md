# Restaurant Details Microservice

This repository contains an AWS Lambda function that retrieves details of a restaurant using the Google Places API.

## Structure

- `lambda_function.py`: The main Lambda function code.
- `requirements.txt`: List of dependencies.
- `.gitignore`: Git ignore file.
- `README.md`: Project description and setup instructions.

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/lambda-function-repo.git
   cd lambda-function-repo
   ```

2. Create a virtual environment:

   ```sh
   python -m venv myenv
   source myenv/bin/activate
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Deactivate the virtual environment:

   ```sh
   deactivate
   ```

5. Package the Lambda function:
   ```sh
   mkdir lambda_package
   cp -r myenv/lib/python3.x/site-packages/* lambda_package/
   cp lambda_function.py lambda_package/
   cd lambda_package
   zip -r ../lambda_function.zip .
   cd ..
   ```
6. Deploy the lambda_function.zip file to AWS Lambda

## Usage

Setup enviroment variables within AWS Lmabda OR replace GOOGLE_PLACES_API_KEY with actual Google API Key.

## License

MIT
