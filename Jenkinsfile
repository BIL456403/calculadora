pipeline {
    agent any

    stages {
        stage('Clonar Repositorio') {
            steps {
                script {
                    // Clonar el repositorio desde GitHub
                    git branch: 'main', url: 'https://github.com/BIL456403/calculadora'
                }
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
                    python3 -m unittest test_calculadora.py
                    '''
                }
            }
        }

        stage('Fallo Intencional con Comando Erróneo') {
            steps {
                script {
                    // Intentar ejecutar un comando que no existe para provocar un fallo
                    sh 'non_existent_command' // Esto provocará un fallo
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
