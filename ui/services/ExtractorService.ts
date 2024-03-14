import ApiService from './ApiService'

export default class ExtractorService {
    _apiService: any

    constructor() {
        this._apiService = new ApiService()
    }

    public async getExtractors() {
        return this._apiService.get('/extractors').then((response: any) => response.json())
    }

    public async getExtractor(uuid: string) {
        return this._apiService.get(`/extractors/${uuid}`)
    }

    public async createExtractor(data: any) {
        return this._apiService.post('/extractors', data)
    }
}