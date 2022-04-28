// script from https://github.com/buonzz/jquery-ph-locations
var handler = {
    fill_provinces:  function(){
        var region_code = $(this).val();
        $('#province').ph_locations('fetch_list', [{"region_code": region_code}]);
        
    },
    fill_cities: function(){
        var province_code = $(this).val();
        $('#city').ph_locations( 'fetch_list', [{"province_code": province_code}]);
    },
    fill_barangays: function(){
        var city_code = $(this).val();
        $('#barangay').ph_locations('fetch_list', [{"city_code": city_code}]);
    }
};
$(function(){
    $('#region').on('change', handler.fill_provinces);
    $('#province').on('change', handler.fill_cities);
    $('#city').on('change', handler.fill_barangays);
    $('#region').ph_locations({'location_type': 'regions'});
    $('#province').ph_locations({'location_type': 'provinces'});
    $('#city').ph_locations({'location_type': 'cities'});
    $('#barangay').ph_locations({'location_type': 'barangays'});
    $('#region').ph_locations('fetch_list');
});
// test code for translating into name
function getRegion(){
    $("#region :selected").text();
}
function getProvince(){
    $("#province :selected").text();
}
function getCity(){
    $("#city :selected").text();
}
function getBarangay(){
    $("#barangay :selected").text();
}
