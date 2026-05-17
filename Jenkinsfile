pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Deploy Web App') {
            steps {
                // 1. Kill the old calculator server if it is already running so we can update it
                sh 'pkill -f "python3 Calculator.py" || true'
                
                // 2. Start the new calculator server in the background. 
                // JENKINS_NODE_COOKIE stops Jenkins from accidentally killing our app when the pipeline finishes.
                sh 'JENKINS_NODE_COOKIE=dontKillMe nohup python3 Calculator.py > app.log 2>&1 &'
                
                echo 'Calculator is now deployed and running on Port 5000!'
            }
        }
    }
}