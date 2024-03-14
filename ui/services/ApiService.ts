export default class ApiService {
    baseUrl = 'http://localhost:8000'

    public async call(url: string, method: string, data?: any, params = {}) {
        url = this.baseUrl + url
        return fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data),
            ...params
        })
    }

    public async get(url: string, params = {}) {
        return this.call(url, 'GET', undefined, params)
    }

    public async post(url: string, data: any, params = {}) {
        return this.call(url, 'POST', data, params)
    }

    public async put(url: string, data: any, params = {}) {
        return this.call(url, 'PUT', data, params)
    }

    public async delete(url: string, params = {}) {
        return this.call(url, 'DELETE', undefined, params)
    }
}