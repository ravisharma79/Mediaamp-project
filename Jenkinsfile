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
                sh 'sudo systemctl restart flask-app.service'
            }
        }

        stage('Hit Endpoint') {
            steps {
                sh 'curl -s http://127.0.0.1:5000/ || true'
            }
        }
    }
}
