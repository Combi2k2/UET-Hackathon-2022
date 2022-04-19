from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

location = geolocator.geocode('hà nam')

print(location)

x = location.raw['lat']
y = location.raw['lon']

print(x, y)


address_Hanoi = ['hn',
                 'tt138a giảng vừ',
                 'hai bà t',
                 'ngõ 409 kim mã',
                 'láng hạ',
                 'thanh oai',
                 'hà tây',
                 'hà đông',
                 'ngõ 379 phố hoàng hoa thám',
                 'khu đô thị mới dịch vọng',
                 'tòa nhà lotte center',
                 'a mandarin garden hoàng minh giám',
                 'hà nộ',
                 'khu chung cư việt hưng',
                 'ngõ 668 đường lạc long quân',
                 'tp ha nô i',
                 '1 khu đt việt hưng',
                 'hà n i',
                 'th nh phè h néi',
                 'đống đa',
                 'h1 tt qđ phương mai',
                 'hà nam',
                 'hn.',
                 'ngách 445 42 đường nguyễn khang',
                 'lô cc6 khu dịch vụ tổng hợp và nhà ở hồ linh đàm',
                 'ngõ 140 1 6 nguyễn xiển',
                 'ngách 71 46 hoàng văn thái',
                 'quận thanh',
                 'hà nội 52743',
                 'chung cư chelsea park',
                 'khu tỏi định cư đường 32',
                 'ngõ 11 tổ dân phố số 4',
                 'tổ dân phố số 6',
                 'thôn ngãi cầu',
                 'thôn dương cốc']

address_HoaBinhf = ['t hòa bình',
                    't. hòa bình',
                    't.hoà bình',
                    'hb']