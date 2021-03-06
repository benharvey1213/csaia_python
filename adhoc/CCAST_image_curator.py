import os
import exifread
from GPSPhoto import gpsphoto

supported_formats = ('.jpg', '.jpeg', '.tif', '.tiff')


def none_check_str(val):
    return None if val is None else str(val)


def none_check_float(val):
    return None if val is None else float(val)


def none_check_int(val):
    return None if val is None else int(str(val))


def curate(dir):
    file = open("bulk_upload_query.txt", "a")
    file.write("\nINSERT INTO")
    file.write("\nimages(user_id, flight_id, directory_location, image_extension, datetime, latitude, longitude, altitude, image_width, image_height, exposure_time, f_number, iso_speed, metering_mode, focal_length, light_source, exposure_mode, white_balance, gain_control, contrast, saturation, sharpness, image_compression, exif_version, software_version, hardware_make, hardware_model, hardware_serial_number)")
    file.write("\nVALUES")
    file.close()
    for root, subdirs, files in os.walk(dir):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in supported_formats:
                imgPath = os.path.join(root, file)
                tags = exifread.process_file(open(imgPath, 'rb'))
                gpsData = gpsphoto.getGPSData(imgPath)

                latitude = none_check_float(gpsData.get('Latitude'))
                longitude = none_check_float(gpsData.get('Longitude'))
                altitude = none_check_float(gpsData.get('Altitude'))
                date_time = none_check_str(tags.get('Image DateTime'))
                exposure_time = none_check_str(tags.get('EXIF ExposureTime'))
                f_number = none_check_str(tags.get('EXIF FNumber'))
                metering_mode = none_check_str(tags.get('EXIF MeteringMode'))
                focal_length = none_check_str(tags.get('EXIF FocalLength'))
                exif_version = none_check_str(tags.get('EXIF ExifVersion'))
                software_version = none_check_str(tags.get('Image Software'))
                hardware_make = none_check_str(tags.get('Image Make'))
                hardware_model = none_check_str(tags.get('Image Model'))
                hardware_serial_number = none_check_str(tags.get('EXIF BodySerialNumber'))
                light_source = none_check_str(tags.get('EXIF LightSource'))
                white_balance = none_check_str(tags.get('EXIF WhiteBalance'))
                gain_control = none_check_str(tags.get('EXIF GainControl'))
                contrast = none_check_str(tags.get('EXIF Contrast'))
                saturation = none_check_str(tags.get('EXIF Saturation'))
                sharpness = none_check_str(tags.get('EXIF Sharpness'))
                image_compression = none_check_str(tags.get('Image Compression'))

                image_height = none_check_int(tags.get('Image ImageWidth')) or none_check_int(tags.get('EXIF ExifImageWidth'))
                image_width = none_check_int(tags.get('Image ImageLength')) or none_check_int(tags.get('EXIF ExifImageLength'))
                iso_speed = none_check_int(tags.get('EXIF ISOSpeed')) or none_check_int(tags.get('EXIF ISOSpeedRatings'))
                exposure_mode = none_check_str(tags.get('EXIF ExposureProgram')) or none_check_str(tags.get('EXIF ExposureMode'))
                file = open("bulk_upload_query.txt", "a")
                file.write("\n(NULL, NULL, '"+str(imgPath)+"', '"+str(ext)+"', '"+str(date_time)+"', '"+str(latitude)+"', '"+str(longitude)+"', "+str(altitude)+", "+str(image_width)+", "+str(image_height)+", '"+str(exposure_time)+"', '"+str(f_number)+"', "+str(iso_speed)+", '"+str(metering_mode)+"', '"+str(focal_length)+"', '"+str(light_source)+"', '"+str(exposure_mode)+"', '"+str(white_balance)+"', '"+str(gain_control)+"', '"+str(contrast)+"', '"+str(saturation)+"', '"+str(sharpness)+"', '"+str(image_compression)+"', '"+str(exif_version)+"', '"+str(software_version)+"', '"+str(hardware_make)+"', '"+str(hardware_model)+"', '"+str(hardware_serial_number)+"'),")
                file.close()

                del imgPath
                del tags
                del gpsData
                del latitude
                del longitude
                del altitude
                del date_time
                del exposure_time
                del f_number
                del metering_mode
                del focal_length
                del exif_version
                del software_version
                del hardware_make
                del hardware_model
                del hardware_serial_number
                del light_source
                del white_balance
                del gain_control
                del contrast
                del saturation
                del sharpness
                del image_compression
                del image_height
                del image_width
                del iso_speed
                del exposure_mode
            del ext
    file.close()


curate(os.path.dirname(os.path.realpath(__file__)))
