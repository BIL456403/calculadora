pipeline {
    agent any

    stages {
        stage('Clonar Repositorio') {
            steps {
                // Clonar el repositorio desde GitHub
                git url: 'https://github.com/BIL456403/calculadora'
            }
        }

        stage('Verificar Python y pip') {
            steps {
                script {
                    // Verificar versiones de Python y pip
                    sh 'python3 --version'
                    sh 'pip3 --version'
                }
            }
        }

        stage('Crear Entorno Virtual y Instalar Dependencias') {
            steps {
                script {
                    // Crear entorno virtual
                    sh 'python3 -m venv venv'

                    // Instalar dependencias con pip dentro del entorno virtual
                    sh '''
                    . venv/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                script {
                    // Ejecutar pruebas dentro del entorno virtual
                    sh '''
                    . venv/bin/activate
                    python3 -m unittest test_calculator.py
                    '''
                }
            }
        }
    }

    post {
        success {
            echo '¡Pruebas exitosas!'
        }
        failure {
            echo 'Las pruebas fallaron.'
        }
    }
}
