# Variable Groups
var_group_dict = {
    "var_group_temperature": [
        "2m_dewpoint_temperature",
        "2m_temperature",
        "skin_temperature",
        "soil_temperature_level_1",
        "soil_temperature_level_2",
        "soil_temperature_level_3",
        "soil_temperature_level_4"
        ],
    "var_group_lake": [
        "lake_bottom_temperature",
        "lake_ice_depth",
        "lake_ice_temperature",
        "lake_mix_layer_depth",
        "lake_mix_layer_temperature",
        "lake_shape_factor",
        "lake_total_layer_temperature"
        ],
    "var_group_snow": [
        "snow_albedo",
        "snow_cover",
        "snow_density",
        "snow_depth",
        "snow_depth_water_equivalent",
        "snowfall",
        "snowmelt",
        "temperature_of_snow_layer"
        ],
    "var_group_soil_water": [
        "skin_reservoir_content",
        "volumetric_soil_water_layer_1",
        "volumetric_soil_water_layer_2",
        "volumetric_soil_water_layer_3",
        "volumetric_soil_water_layer_4"
        ],
    "var_group_radiation_and_heat": [
        "forecast_albedo",
        "surface_latent_heat_flux",
        "surface_net_solar_radiation",
        "surface_net_thermal_radiation",
        "surface_sensible_heat_flux",
        "surface_solar_radiation_downwards",
        "surface_thermal_radiation_downwards"
        ],
    "var_group_evaporation_and_runoff": [
        "evaporation_from_bare_soil",
        "evaporation_from_open_water_surfaces_excluding_oceans",
        "evaporation_from_the_top_of_canopy",
        "evaporation_from_vegetation_transpiration",
        "potential_evaporation",
        "runoff",
        "snow_evaporation",
        "sub_surface_runoff",
        "surface_runoff",
        "total_evaporation"
        ],
    "var_group_wind_pressure_and_precipitation": [
        "10m_u_component_of_wind",
        "10m_v_component_of_wind",
        "surface_pressure",
        "total_precipitation"
    ],
    "var_group_vegetation": [
        "leaf_area_index_high_vegetation",
        "leaf_area_index_low_vegetation"
        ]
}

# List of variable group
var_group_name_list = ['var_group_temperature',
                        'var_group_lake',
                        'var_group_snow',
                        'var_group_soil_water',
                        'var_group_radiation_and_heat',
                        'var_group_evaporation_and_runoff',
                        'var_group_wind_pressure_and_precipitation',
                        'var_group_vegetation']