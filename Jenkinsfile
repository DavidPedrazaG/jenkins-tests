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
                    pip install pytest-html
                """
            }
        }

        stage('Tests') {
            steps {
                sh """
                    . venv/bin/activate
                    # Ejecuta tests y genera XML para Jenkins
                    pytest --junitxml=results.xml --log-cli-level=INFO
                    # Genera el reporte HTML con pytest-html
                    pytest --html=report.html --self-contained-html
                """
            }
        }
    }

    post {
        always {
            
            junit 'results.xml'

        
            publishHTML([allowMissing: false,
                         alwaysLinkToLastBuild: true,
                         keepAll: true,
                         reportDir: '.',          
                         reportFiles: 'report.html',
                         reportName: 'Test Report'])
        }
    }
}
