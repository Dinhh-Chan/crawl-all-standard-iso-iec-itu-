import requests 
import  json
def get_all_standard():
    #iso 
    def iso():
        URL = "https://jcl49wv5ar-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.22.1)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.64.3)%3B%20JS%20Helper%20(3.16.2)&x-algolia-api-key=MzcxYjJlODU3ZmEwYmRhZTc0NTZlODNlZmUwYzVjNDRiZDEzMzRjMjYwNTAwODU3YmIzNjEwZmNjNDFlOTBjYXJlc3RyaWN0SW5kaWNlcz1QUk9EX2lzb29yZ19lbiUyQ1BST0RfaXNvb3JnX2VuX2F1dG9jb21wbGV0ZQ%3D%3D&x-algolia-application-id=JCL49WV5AR"
        data = []
        page = 0
        links=[]
        while True :
            
            json_data = {
                    "requests": [
                        {
                            "indexName": "PROD_isoorg_en",
                            "params": f"clickAnalytics=true&facetFilters=%5B%5B%22facet%3Astandard%22%5D%5D&facets=%5B%22facet%22%5D&highlightPostTag=__%2Fais-highlight__&highlightPreTag=__ais-highlight__&maxValuesPerFacet=10&page={page}&query=iec&tagFilters=&userToken=anonymous-091345c9-5a26-40a9-b501-3bcf5177ba7d"
                        }
                    ]
                }
            r = requests.post(url=URL, json=json_data)

                # extracting data in json format
            data = r.json()['results'][0]['hits']
            for i in data:
                standard = {
                "Số hiệu tiêu chuẩn": i['reference'],
                "Tên tiểu chuẩn" : i["title"],
                "Năm ban hành": i['lastIndexation'],
                "Đường link": "https://www.iso.org/"+ i['seoURL'],
                "Trạng thái":i['statusKey'],
                "File tiêu chuẩn": "N/A",
            
                }
                print(standard)
                links.append(standard)
            page +=1
            if page == 222:
                break
        return links
    #itu 
    def itu():
        #recommendations-recommendations
        def retrieve_recommendations():
            url = "https://www.itu.int/net4/ITU-T/search/GlobalSearch/RunSearch"
            page = 0
            arr_standard = []

            while True:
                payload = {
                    "Input": "iec",
                    "Start": page,
                    "Rows": 10,
                    "SortBy": "RELEVANCE",
                    "ExactPhrase": False,
                    "CollectionName": "ITU-T Recommendations",
                    "CollectionGroup": "Recommendations",
                    "Sector": "t",
                    "Criterias": [
                        {
                            "Name": "Search in ITU-T Recommendations",
                            "Criterias": [
                                {"Selected": False, "Value": "", "Label": "Persistent ID", "Target": "\/persistent_identifier_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:108"},
                                {"Selected": False, "Value": "", "Label": "Name", "Target": "\/name_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:109"},
                                {"Selected": False, "Value": "", "Label": "Title", "Target": "\/subject_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:110"},
                                {"Selected": False, "Value": "", "Label": "Content", "Target": "\/file", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:111"}
                            ],
                            "ShowCheckbox": True,
                            "Selected": False,
                            "$$hashKey": "object:49"
                        },
                        {
                            "Name": "Type",
                            "Criterias": [
                                {"Selected": False, "Value": "Administrative Document", "Label": "Administrative Document", "Target": "\/object_type_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:140"},
                                {"Selected": False, "Value": "Circular", "Label": "Circular", "Target": "\/object_type_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:141"},
                                {"Selected": False, "Value": "Collective letter", "Label": "Collective letter", "Target": "\/object_type_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:142"},
                                {"Selected": False, "Value": "Contribution", "Label": "Contribution", "Target": "\/object_type_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:143"},
                                {"Selected": False, "Value": "Information Document", "Label": "Information Document", "Target": "\/object_type_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:144"},
                                {"Selected": False, "Value": "Report", "Label": "Report", "Target": "\/object_type_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:145"},
                                {"Selected": False, "Value": "Temporary Document", "Label": "Temporary Document", "Target": "\/object_type_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:146"},
                                {"Selected": False, "Value": "Other", "Label": "Other", "Target": "\/object_type_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:147"}
                            ],
                            "ShowCheckbox": True,
                            "Selected": False,
                            "$$hashKey": "object:50"
                        },
                        {
                            "Name": "Date",
                            "Criterias": [
                                {"FromDateString": "1900-01-01T00:00:00Z", "ToDateString": "2024-04-13T10:50:37Z", "Label": None, "Target": "\/object_date_d", "TypeName": "DATERANGE", "GetCriteriaType": 2, "From": "1900-01-01T00:00:00.000Z", "To": "2024-04-13T10:50:12.000Z", "$$hashKey": "object:196"}
                            ],
                            "ShowCheckbox": False,
                            "Selected": False,
                            "$$hashKey": "object:51"
                        }
                    ],
                    "Topics": "",
                    "ClientData": {"as": "AS45899 VNPT Corp", "city": "Hanoi", "country": "Vietnam", "countryCode": "VN", "isp": "VNPT", "lat": 21.0292, "lon": 105.8526, "org": "Vietnam Posts and Telecommunications Group", "query": "14.177.225.128", "region": "HN", "regionName": "Hanoi", "status": "success", "timezone": "Asia/Bangkok", "zip": ""},
                    "Language": "en",
                    "IP": "14.177.225.128",
                    "SearchType": "All"
                }

                json_data = json.dumps(payload)
                form_data = {'json': json_data}

                response = requests.post(url, data=form_data)

                if response.status_code == 200:
                    data = response.json()
                    if not data['results']:
                        break  # No more results, exit the loop
                    for i in data['results']:
                        tt = i['Title'].split('|')
                        new_data = {
                            "Số hiệu tiêu chuẩn": tt[0],
                            "Tên tiêu chuẩn": i['Title'],
                            "Tên tiểu chuẩn(Tiếng quốc gia ban hành)": i['Title'],
                            "Năm ban hành": i["Properties"][0]['Value'],
                            "Đường link": 'https://www.itu.int/rec/T-REC-' + tt[0].split()[1],
                            "File tiêu chuẩn": "N/A"
                        }
                        arr_standard.append(new_data)
                else:
                    print("Failed to retrieve data:", response.status_code)

                page += 10

            return arr_standard
        #meetingdoument-laisionstatement    
        def metting_laision():
            arr_standard=[]
            url = "https://www.itu.int/net4/ITU-T/search/GlobalSearch/RunSearch"

            page = 0 
            rows_per_page = 10  # Number of results per page

            while True:
                payload = {
                    "Input": "iec",
                    "Start": page,
                    "Rows": rows_per_page,
                    "SortBy": "RELEVANCE",
                    "ExactPhrase": False,
                    "CollectionName": "ITU-T Meeting Documents",
                    "CollectionGroup": "ITU-T Liaison Statement",
                    "Sector": "t",
                    "Criterias": [
                        {
                            "Name": "Search in ITU-T Meeting Documents",
                            "Criterias": [
                                {"Selected": False, "Value": "", "Label": "Persistent ID", "Target": "\/persistent_identifier_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:108"},
                                {"Selected": False, "Value": "", "Label": "Name", "Target": "\/name_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:109"},
                                {"Selected": False, "Value": "", "Label": "Title", "Target": "\/subject_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:110"},
                                {"Selected": False, "Value": "", "Label": "Content", "Target": "\/file", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:111"}
                            ],
                            "ShowCheckbox": True,
                            "Selected": False,
                            "$$hashKey": "object:49"
                        },
                        {
                            "Name": "Type",
                            "Criterias": [
                                {"Selected": False, "Value": "Administrative Document", "Label": "Administrative Document", "Target": "\/object_type_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:140"},
                                {"Selected": False, "Value": "Circular", "Label": "Circular", "Target": "\/object_type_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:141"},
                                {"Selected": False, "Value": "Collective letter", "Label": "Collective letter", "Target": "\/object_type_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:142"},
                                {"Selected": False, "Value": "Contribution", "Label": "Contribution", "Target": "\/object_type_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:143"},
                                {"Selected": False, "Value": "Information Document", "Label": "Information Document", "Target": "\/object_type_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:144"},
                                {"Selected": False, "Value": "Report", "Label": "Report", "Target": "\/object_type_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:145"},
                                {"Selected": False, "Value": "Temporary Document", "Label": "Temporary Document", "Target": "\/object_type_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:146"},
                                {"Selected": False, "Value": "Other", "Label": "Other", "Target": "\/object_type_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:147"}
                            ],
                            "ShowCheckbox": True,
                            "Selected": False,
                            "$$hashKey": "object:50"
                        },
                        {
                            "Name": "Date",
                            "Criterias": [
                                {"FromDateString": "1900-01-01T00:00:00Z", "ToDateString": "2024-04-13T10:47:15Z", "Label": None, "Target": "\/object_date_d", "TypeName": "DATERANGE", "GetCriteriaType": 2, "From": "1900-01-01T00:00:00.000Z", "To": "2024-04-13T10:46:54.000Z", "$$hashKey": "object:196"}
                            ],
                            "ShowCheckbox": False,
                            "Selected": False,
                            "$$hashKey": "object:51"
                        }
                    ],
                    "Topics": "",
                    "ClientData": {"as": "AS45899 VNPT Corp", "city": "Hanoi", "country": "Vietnam", "countryCode": "VN", "isp": "VNPT", "lat": 21.0292, "lon": 105.8526, "org": "Vietnam Posts and Telecommunications Group", "query": "14.177.225.128", "region": "HN", "regionName": "Hanoi", "status": "success", "timezone": "Asia/Bangkok", "zip": ""},
                    "Language": "en",
                    "IP": "14.177.225.128",
                    "SearchType": "All"
                }

                json_data = json.dumps(payload)
                form_data = {'json': json_data}

                response = requests.post(url, data=form_data)

                if response.status_code == 200:
                    data = response.json()
                    print(json.dumps(data, indent=4))  # Print data for debugging
                    if not data['results']:
                        break  # No more results, exit the loop
                    for i in data['results']:
                        tt = i['Title'].split(':')
                        new_data = {
                            "Số hiệu tiêu chuẩn": tt[0],
                            "Tên tiêu chuẩn(Tiếng Anh)": i['Title'],
                            "Tên tiêu chuẩn(Tiếng quốc gia ban hành)": i['Title'],
                            "Năm ban hành": i["Properties"][0]['Value'],
                            "Đường link": 'https://www.itu.int/' + i["Redirection"],
                            "File tiêu chuẩn": "N/A"
                        }
                        arr_standard.append(new_data)  # Print each new data entry for debugging
                else:
                    print("Failed to retrieve data:", response.status_code)

                page += rows_per_page
                if page ==2220 :
                    break
            return arr_standard
        #meeting-metting
        def metting_metting():
            url = "https://www.itu.int/net4/ITU-T/search/GlobalSearch/RunSearch"
            arr_standard = []
            page = 0
            rows_per_page = 10  # Number of results per page

            while True:
                payload = {
                    "Input": "iec",
                    "Start": page,  # Dynamically set the start index
                    "Rows": rows_per_page,
                    "SortBy": "RELEVANCE",
                    "ExactPhrase": False,
                    "CollectionName": "ITU-T Meeting Documents",
                    "CollectionGroup": "Meeting Documents",
                    "Sector": "t",
                    "Criterias": [
                        {
                            "Name": "Search in ITU-T Meeting Documents",
                            "Criterias": [
                                {"Selected": False, "Value": "", "Label": "Persistent ID", "Target": "\/persistent_identifier_s",
                                "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:108"},
                                {"Selected": False, "Value": "", "Label": "Name", "Target": "\/name_s", "TypeName": "CHECKBOX",
                                "GetCriteriaType": 0, "$$hashKey": "object:109"},
                                {"Selected": False, "Value": "", "Label": "Title", "Target": "\/subject_s", "TypeName": "CHECKBOX",
                                "GetCriteriaType": 0, "$$hashKey": "object:110"},
                                {"Selected": False, "Value": "", "Label": "Content", "Target": "\/file", "TypeName": "CHECKBOX",
                                "GetCriteriaType": 0, "$$hashKey": "object:111"}
                            ],
                            "ShowCheckbox": True,
                            "Selected": False,
                            "$$hashKey": "object:49"
                        },
                        {
                            "Name": "Type",
                            "Criterias": [
                                {"Selected": False, "Value": "Administrative Document", "Label": "Administrative Document",
                                "Target": "\/object_type_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0,
                                "$$hashKey": "object:140"},
                                {"Selected": False, "Value": "Circular", "Label": "Circular", "Target": "\/object_type_s",
                                "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:141"},
                                {"Selected": False, "Value": "Collective letter", "Label": "Collective letter",
                                "Target": "\/object_type_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0,
                                "$$hashKey": "object:142"},
                                {"Selected": False, "Value": "Contribution", "Label": "Contribution", "Target": "\/object_type_s",
                                "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:143"},
                                {"Selected": False, "Value": "Information Document", "Label": "Information Document",
                                "Target": "\/object_type_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0,
                                "$$hashKey": "object:144"},
                                {"Selected": False, "Value": "Report", "Label": "Report", "Target": "\/object_type_s",
                                "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:145"},
                                {"Selected": False, "Value": "Temporary Document", "Label": "Temporary Document",
                                "Target": "\/object_type_s", "TypeName": "CHECKBOX", "GetCriteriaType": 0,
                                "$$hashKey": "object:146"},
                                {"Selected": False, "Value": "Other", "Label": "Other", "Target": "\/object_type_s",
                                "TypeName": "CHECKBOX", "GetCriteriaType": 0, "$$hashKey": "object:147"}
                            ],
                            "ShowCheckbox": True,
                            "Selected": False,
                            "$$hashKey": "object:50"
                        },
                        {
                            "Name": "Date",
                            "Criterias": [
                                {"FromDateString": "1900-01-01T00:00:00Z", "ToDateString": "2024-04-13T10:47:15Z", "Label": None,
                                "Target": "\/object_date_d", "TypeName": "DATERANGE", "GetCriteriaType": 2,
                                "From": "1900-01-01T00:00:00.000Z", "To": "2024-04-13T10:46:54.000Z", "$$hashKey": "object:196"}
                            ],
                            "ShowCheckbox": False,
                            "Selected": False,
                            "$$hashKey": "object:51"
                        }
                    ],
                    "Topics": "",
                    "ClientData": {"as": "AS45899 VNPT Corp", "city": "Hanoi", "country": "Vietnam", "countryCode": "VN",
                                "isp": "VNPT", "lat": 21.0292, "lon": 105.8526, "org": "Vietnam Posts and Telecommunications Group",
                                "query": "14.177.225.128", "region": "HN", "regionName": "Hanoi", "status": "success",
                                "timezone": "Asia/Bangkok", "zip": ""},
                    "Language": "en",
                    "IP": "14.177.225.128",
                    "SearchType": "All"
                }

                json_data = json.dumps(payload)
                form_data = {'json': json_data}
                response = requests.post(url, data=form_data)

                if response.status_code == 200:
                    data = response.json()
                    if not data['results']:
                        break  # No more results, exit the loop
                    for i in data['results']:
                        tt = i['Title'].split(':')
                        new_data = {
                            "Số hiệu tiêu chuẩn": tt[0],
                            "Tên tiêu chuẩn(Tiếng Anh)": i['Title'],
                            "Tên tiêu chuẩn(Tiếng quốc gia ban hành)": i['Title'],
                            "Năm ban hành": i["Properties"][0]['Value'],
                            "Đường link": 'https://www.itu.int' + i["Redirection"],
                            "File tiêu chuẩn": "N/A"
                            
                        }
                        print(new_data)
                        arr_standard.append(new_data)
                else:
                    print("Failed to retrieve data:", response.status_code)

                page += rows_per_page
                if page == 57890 :
                    break
            return arr_standard
        
    #publication
        def publication():
            url = "https://www.itu.int/net4/ITU-T/search/GlobalSearch/RunSearch"
            arr_standard = []
            page = 0
            rows_per_page = 10  # Number of results per page

            while True:
                payload = {
                "Input": "iec",
                "Start": page,
                    "Rows": 10,
                    "SortBy": "RELEVANCE",
                    "ExactPhrase": False,
                    "CollectionName": "ITU-T Publications",
                    "CollectionGroup": "Publications",
                    "Sector": "t",
                    "Criterias": [
                        {"Name": "Search in", "Criterias": [
                            {"Selected": False, "Value": "", "Label": "Name", "Target": "/name_s", "TypeName": "CHECKBOX"},
                            {"Selected": False, "Value": "", "Label": "Short description", "Target": "/short_description_s", "TypeName": "CHECKBOX"},
                            {"Selected": False, "Value": "", "Label": "File content", "Target": "/file", "TypeName": "CHECKBOX"}
                        ], "ShowCheckbox": True}
                    ],
                    "Topics": "",
                    "ClientData": {
                        "as": "AS45899 VNPT Corp",
                        "city": "Hanoi",
                        "country": "Vietnam",
                        "countryCode": "VN",
                        "isp": "VNPT",
                        "lat": 21.0292,
                        "lon": 105.8526,
                        "org": "Vietnam Posts and Telecommunications Group",
                        "query": "14.177.225.128",
                        "region": "HN",
                        "regionName": "Hanoi",
                        "status": "success",
                        "timezone": "Asia/Bangkok",
                        "zip": ""
                    },
                    "Language": "en",
                    "IP": "14.177.225.128",
                    "SearchType": "All"
                }

                json_data = json.dumps(payload)
                form_data = {'json': json_data}
                response = requests.post(url, data=form_data)

                if response.status_code == 200:
                    data = response.json()
                    if not data['results']:
                        break  # No more results, exit the loop
                    for i in data['results']:
                        tt = i['Title'].split(':')
                        new_data = {
                                "Số hiệu tiêu chuẩn": tt[0],
                                "Tên tiêu chuẩn(Tiếng Anh)": i['Title'],
                                "Tên tiêu chuẩn(Tiếng quốc gia ban hành)": i['Title'],
                                "Năm ban hành": i["Properties"][0]['Value'],
                                "Đường link": 'https://www.itu.int' + i["Redirection"],
                                "File tiêu chuẩn": "N/A"
                            }
                        
                        arr_standard.append(new_data)
                    else:
                        print("Failed to retrieve data:", response.status_code)

                    page += rows_per_page
                    if page == 57890 :
                        break
                return arr_standard
        arr_standard= metting_metting()+ metting_laision() + retrieve_recommendations()+publication()
        return arr_standard
    def iec():
        import requests
        from bs4 import BeautifulSoup
        url = "https://www.iec.ch/technical-committees-and-subcommittees#tclist"
        response = requests.get(url)
        arr_standard = []
        # Kiểm tra xem yêu cầu thành công hay không
        if response.status_code == 200:
            # Parse HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Tìm tất cả các thẻ <td> có class là "datatable-column-publications"
            td_tags = soup.find_all('td', class_='datatable-column-publications')
            
            # Lấy các liên kết từ các thẻ <a> bên trong các thẻ <td>
            links = ['https://www.iec.ch'+ td.find('a')['href'] for td in td_tags if td.find('a')]
            for i in links :
                response= requests.get(i)
                soup =  BeautifulSoup(response.content, 'html.parser')
                div_tag =soup.find_all('div', class_='pad10')
                standard = [div.find('a')['href'] for div in div_tag if div.find('a')]
                for j in standard :
                    response= requests.get(j)
                    soup =  BeautifulSoup(response.content, 'html.parser')
                    id = soup.find('h1', class_='reference')
                    title = soup.find('h2', class_='title')
                    pub_date = soup.find(id="view:inputText3")
                    abstract = soup.find(id="view:computedField3")
                    data = {
                        "Số hiệu tiêu chuẩn": id.text.strip(),
                        "Tên tiêu chuẩn": title.text.strip(),
                        "Tên tiêu chuẩn (tiếng quốc gia ban hành)": title.text.strip(),
                        "Năm ban hành": pub_date.text.strip(),
                        "Đường link" : j,
                        "File tiêu chuẩn": "N/A",
                        "Tóm tắt": abstract.text.strip()
                        
                    }
                    arr_standard.append(data)
            print(links)
        else:
            print("Yêu cầu không thành công!")
        return  arr_standard
    sum_standard = itu()+ iso() + iec()
    return sum_standard
if __name__=='__main__':
    standard = get_all_standard()
    
