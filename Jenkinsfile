pipeline {
    agent any

    environment {
        IMAGE_NAME = "mirzomumin/flaskapp"
        IMAGE_TAG = "latest"
        REMOTE_HOST = "ubuntu@37.9.53.88"
        REMOTE_DIR = "/home/ubuntu/flaskapp"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        stage('Lint/Test') {
            steps {
                sh """
                    docker run --rm -v $(pwd):/app -w /app python:3.10-slim bash -c '
                        pip install --no-cache-dir ruff &&
                        ruff check .
                    '
                """
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${IMAGE_NAME}:${IMAGE_TAG}
                    """
                }
            }
        }

        stage('Deploy to Remote Server') {
            steps {
                sshagent (credentials: ['ssh-credentials-id']) {
                    sh """
                        ssh -o StrictHostKeyChecking=no ${REMOTE_HOST} '
                            docker pull ${IMAGE_NAME}:${IMAGE_TAG} &&
                            cd ${REMOTE_DIR} &&
                            docker-compose down &&
                            docker-compose up -d
                        '
                    """
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
