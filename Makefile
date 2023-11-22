docker:
	docker build --build-arg API_KEY=${OPENAI_API_KEY} --tag moviegpt .

run:
	docker run -p 8000:8000 -e "OPENAI_API_KEY=${OPENAI_API_KEY}" moviegpt 