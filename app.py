from flask import Flask, render_template, jsonify
import boto3

app = Flask(__name__)

# DynamoDB setup
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('TemperatureData')

# Endpoint to get temperature data
@app.route('/temperature', methods=['GET'])
def get_temperature():
    response = table.scan()  # Retrieve all records
    items = response['Items']
    return jsonify(items)

# Endpoint to view the dashboard
@app.route('/')
def index():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
