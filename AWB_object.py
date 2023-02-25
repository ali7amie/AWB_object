import numpy as np
import pandas as pd


class TIR:

    def __init__(self,TIR_number):
      self.TIR_number=TIR_number



class AWB:

    '''
        This class take each AWB, DO, and TIR data, in ordre to create a database. It include what I call super setter where all information inside a 
        commercial documents are entered together in an array. after that individual setter and getter take these pieces of information. Fore the moment
        the class has no heritance but it is associated to the TIR class in order to simplifying the data entry as a TIR include many airwaybills. The 
        init function take the airwaybill number.

        Attributes
        -----------

        AWB_prefix : int

        AWB_serial : int

        AWB_array : list

                    ['shipper_name','shipper_city','shipper_country','consignee_name','consignee_city','consignee_country','agent_name','agent_city','departure_airport','destination_airport','layover_airport','by_first_career[AF 566/12]','flight[AF 566/12','number_of_packages','commodity','gross_weight','chargeable_weight','weight_unit','dimension','rate','rate_class','charge','currency','valuation','tax','total_prepaid','total_collect','issuing_date']

                                 
    '''



    def __init__(self,AWB_prefix,AWB_serial):#,TIR_number):

      #self.TIR_number=TIR_number
      #self.TIR = TIR(self.TIR_number)
      self.AWB_prefix=AWB_prefix
      self.AWB_serial=AWB_serial

      # self.shipper_name=''
      # self.shipper_city=''
      # self.shipper_country=''
      # self.consignee_name=''
      # self.consignee_city=''
      # self.consignee_country=''
      # self.agent_name=''
      # self.agent_city=''
      # self.departure_airport=''
      # self.destination_airport=''
      # self.layover_airport=''
      # self.by_first_career=''
      # self.flight=''
      # self.number_of_packages=0
      # self.commodity=''
      # self.gross_weight=0.0
      # self.chargeable_weight=0.0
      # self.weight_unit=''
      # self.dimension=''
      # self.rate=0.0
      # self.rate_class=''
      # self.charge=0.0
      # self.currency=''
      # self.valuation=0.0
      # self.tax=0.0
      # self.total_prepaid=0.0
      # self.total_collect=0.0
      # self.AWB_issuing_date=''

      # self.flight_number=''
      # self.flight_date=''
      # self.manifest=''
      # self.agent=''
      # self.DO_issuing_date=''



      '''
      This function create an AWB object instance by taking the AWB number divided in two variables, the prefix, and the serial (including the digit)


      Attributes
      -----------
      AWB_prefix : int
                the 3 digit IATA prefix of the airline
      AWB_serial: int
                8 digit AWB number 
      TIR_number: string                  
      Return
      -------
      AWB : object

      '''  


      
    def set_AWB_info(self,shipper_name,shipper_city,shipper_country,consignee_name,consignee_city,consignee_country,agent_name,agent_city,departure_airport,destination_airport,layover_airport,by_first_career,flight,number_of_packages,commodity,gross_weight,chargeable_weight,weight_unit,dimension,rate,rate_class,charge,currency,valuation,tax,total_prepaid,total_collect,AWB_issuing_date):

      self.shipper_name=shipper_name
      self.shipper_city=shipper_city
      self.shipper_country=shipper_country
      self.consignee_name=consignee_name
      self.consignee_city=consignee_city
      self.consignee_country=consignee_country
      self.agent_name=agent_name
      self.agent_city=agent_city
      self.departure_airport=departure_airport
      self.destination_airport=destination_airport
      self.layover_airport=layover_airport
      self.by_first_career=by_first_career
      self.flight=flight
      self.number_of_packages=number_of_packages
      self.commodity=commodity
      self.gross_weight=gross_weight
      self.chargeable_weight=chargeable_weight
      self.weight_unit=weight_unit
      self.dimension=dimension
      self.rate=rate
      self.rate_class=rate_class
      self.charge=charge
      self.currency=currency
      self.valuation=valuation
      self.tax=tax
      self.total_prepaid=total_prepaid
      self.total_collect=total_collect
      self.AWB_issuing_date=AWB_issuing_date


      '''
      This is a what I called super setter, it set all AWB's information at a glance, than transmit it individually to each variable


      Attributes
      -----------
      AWB_array : list
                  ['shipper_name','shipper_city','shipper_country','consignee_name','consignee_city','consignee_country','agent_name','agent_city','departure_airport','destination_airport','layover_airport','by_first_career[AF 566/12]','flight[AF 566/12','number_of_packages','commodity','gross_weight','chargeable_weight','weight_unit','dimension','rate','rate_class','charge','currency','valuation','tax','total_prepaid','total_collect','issuing_date']

      '''  

    def set_DO_info(self,flight_number_DO,flight_date_DO,manifest,DO_agent,DO_issuing_date):

      self.flight_number_DO = flight_number_DO
      self.flight_date_DO = flight_date_DO
      self.manifest = manifest
      self.DO_agent = DO_agent 
      self.DO_issuing_date = DO_issuing_date


      '''
      This is a super setter for DO informations

      Attributes
      -----------
      DO_array : list
                  ['flight_number','flight_date','manifest','agent','issuing_date']

      '''  

    def set_remarks(self,remarks):
      self.remarks=remarks     

    def set_ATS_agent(self,ATS_agent):
      self.ATS_agent=ATS_agent    




['shipper_name','shipper_city','shipper_country','consignee_name','consignee_city','consignee_country','agent_name','agent_city','departure_airport','destination_airport','layover_airport',
 'by_first_career[AF 566/12]','flight[AF 566/12]','number_of_packages','commodity','gross_weight','chargeable_weight','weight_unit','dimension','rate','rate_class','charge','currency','valuation',
 'tax','total_prepaid','total_collect','issuing_date']
