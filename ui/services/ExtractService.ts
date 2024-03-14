import ApiService from "~/services/ApiService";

export default class ExtractService {
    _apiService: any;

    constructor() {
        this._apiService = new ApiService();
    }

    public async extractData(data: any) {
        let formData = new FormData();
        formData.append('extractor_uuid', 'f5a93011-905d-42fc-8a6a-a98acae1e896');
        formData.append('text', data.text);
        formData.append('file', data.file);
        return this._apiService.post('/extract', formData).then((response: any) => response.json());
    }
}