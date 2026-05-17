pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pulls the code from your connected GitHub repository
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building the Python Calculator...'
                // Python is an interpreted language, so a "build" usually involves 
                // compiling it to bytecode to check for syntax errors.
                sh 'python3 -m py_compile calculator.py'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running execution tests...'
                // Simulating a test by executing the script to ensure it runs without crashing
                sh 'python3 calculator.py'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline executed successfully! Application is stable.'
        }
        failure {
            echo 'Pipeline failed. Check the logs for syntax or execution errors.'
        }
    }
}