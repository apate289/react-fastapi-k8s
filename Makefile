.PHONY: build build-backend build-frontend up down k8s-apply helm-install

build-backend:
	docker build -t myapp-backend:local ./backend

build-frontend:
	docker build -t myapp-frontend:local ./frontend

build: build-backend build-frontend

up:
	docker-compose up --build

down:
	docker-compose down

k8s-apply:
	kubectl apply -f k8s/ --recursive

helm-install:
	helm install myapp ./helm-chart -f helm-chart/values.yaml || true
