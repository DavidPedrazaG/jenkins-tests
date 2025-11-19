pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                sh """
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r ./requirements.txt
                """
            }
        }

        stage('Tests') {
            steps {
                sh """
                    . venv/bin/activate
                    pytest --junitxml=results.xml --log-cli-level=INFO
                """
            }
        }
    }

    post {
        always {
            junit 'results.xml'
        }
    }
}
