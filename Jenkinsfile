pipeline {
    agent any
    stages {
		stage('My SonarQube Server') {
			environment {
        		scannerHome = tool 'SonarQubeScanner'
    		}    
			steps {
        		withSonarQubeEnv('sonarqube') {
            		sh "${scannerHome}/bin/sonar-scanner"
				}
        	}
		}
    }
}
