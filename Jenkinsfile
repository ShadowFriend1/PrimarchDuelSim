pipeline {
    agent any
    stages {
		stage('SonarQube analysis') {
			environment {
        		scannerHome = tool 'SonarQubeScanner'
    		}    
			steps {
        		withSonarQubeEnv('My SonarQube Server') {
            		sh "${scannerHome}/bin/sonar-scanner"
				}
        	}
		}
		stage('Checkout Git Comment Program') {
			when {
				changeRequest()
			}
			steps {
				git credentialsId: '33be1895-4822-4709-9977-56ae072efd6f', url: 'https://github.com/ShadowFriend1/pr-Decoration.git'
			}
		}
		stage('Post Pull Request Comment') {
			when {
				changeRequest()
			}
			environment {
				goInstallation = tool 'Go:latest'
				SONARQUBEPROJECT = 'my:project'
				REPO = 'PrimarchDuelSim'
				SONARQUBESERVERLOGIN = credentials('my-sonarqube-server-login')
				PULL_REQ_NUMBER = '$CHANGE_ID'
				SONARQUBEUSER = '$SONARQUBESERVERLOGIN_USR'
				SONARQUBEPASSWORD = '$SONARQUBESERVERLOGIN_PSW'
				GITHUBAPILOGIN = credentials('aab572d0-f1d3-4f9b-b930-812bcb49d485')
				OWNER = '$GITHUBAPILOGIN_USR'
				GITHUB_API_KEY = '$GITHUBAPILOGIN_PSW'
				SONARQUBEURL = withSonarQubeEnv('My SonarQube Server') {
					 sh (returnStdout: true, script: 'echo $SONAR_HOST_URL/').trim() 
				}
			}
			steps {
				withEnv(['GOROOT=${goInstallation}', 'PATH+GO=${goInstallation}/bin']) {
					sh 'go run new.go'
				}
			}
		}
    }
}
