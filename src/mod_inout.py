import xarray as xr
import numpy
import logging

def prep_obs(ds_obs, oi_grid, oi_param, simu_start_date, coarsening):
    
    logging.info('     Preparing observations...')
    
    def preprocess(ds):
        return ds.coarsen(coarsening, boundary="trim").mean()
     
    ds_obs = ds_obs.coarsen(coarsening, boundary="trim").mean().sortby('time')
    
    lon_min = oi_grid.lon.min().values
    lon_max = oi_grid.lon.max().values
    lat_min = oi_grid.lat.min().values
    lat_max = oi_grid.lat.max().values
    time_min = oi_grid.time.min().values
    time_max = oi_grid.time.max().values
    
    
    ds_obs = ds_obs.sel(time=slice(time_min, time_max), drop=True)
    
    
    if lon_min < 0:
        ds_obs['lon'] = xr.where(ds_obs['lon'] >= 180., ds_obs['lon']-360., ds_obs['lon'])
        
    ds_obs = ds_obs.where((ds_obs['lon'] >= lon_min - oi_param.Lx.values) & 
                          (ds_obs['lon'] <= lon_max + oi_param.Lx.values) &
                          (ds_obs['lat'] >= lat_min - oi_param.Ly.values) &
                          (ds_obs['lat'] <= lat_max + oi_param.Ly.values) , drop=True)
    
    vtime = (ds_obs['time'].values - numpy.datetime64(simu_start_date)) / numpy.timedelta64(1, 'h')
    ds_obs = ds_obs.assign_coords({'time': vtime})
    
    return ds_obs



def save_maps(ds_maps,path,dc_ref=None):
    
    logging.info('     Saving reconstruction maps...')
    
    try :
        ds_maps['lon']
        ds_maps['lat']
        ds_maps['time']
        ds_maps['ssh']
    except KeyError:
        print('Warning: For evaluation, the reconstructed maps must contain the coordinates: lon, lat and time and the variable: ssh(time, lat, lon).')
         
    if ds_maps.lon.size != dc_ref.lon.size or ds_maps.lat.size != dc_ref.lat.size or ds_maps.time.size != dc_ref.time.size : 
        print('Warning: For evaluation, the reconstructed maps do not have the same size as the reference maps.')
    elif numpy.any(ds_maps.lon.values != dc_ref.lon.values) or numpy.any(ds_maps.lat.values != dc_ref.lat.values) or numpy.any(ds_maps.time.values != dc_ref.time.values) :  
        print('Warning: For evaluation, the reconstructed maps have the same size as the reference maps but not the same lon, lat or time values.')
         
    
    dsout = xr.Dataset({'ssh':(('time','lat','lon'),ds_maps.ssh.values) 
                       },
                       coords={'time':('time',ds_maps.time.values),'lon':('lon',ds_maps.lon.values),'lat':('lat',ds_maps.lat.values)}
                      )
    dsout.to_netcdf(path)
    
    
    return 