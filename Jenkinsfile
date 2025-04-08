pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}/flask_env"
    }

    stages {
        stage('Set Up Virtualenv') {
            steps {
                sh '''#!/bin/bash
                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirement.txt
                '''
            }
        }

        stage('Restart Flask App') {
            steps {
                sh '''
                    ssh -o StrictHostKeyChecking=no ubuntu@10.0.0.100 'sudo systemctl restart flask-app.service'
                '''
            }
        }

        stage('Hit Endpoint') {
            steps {
                sh 'curl -s http://10.0.0.100/ || true'
            }
        }
    }
}
