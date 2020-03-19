from abc import ABC, abstractmethod
from kafka import KafkaConsumer, KafkaProducer
import json
import os
import LEWSJsonUtil as util


kafka_src_server = os.environ.get("KAFKA_SOURCE_BOOTSTRAP_SERVERS","localhost:9092").split(",")
kafka_src_topic = os.environ.get('KAFKA_SOURCE_TOPIC', 't_topic1')
kafka_tgt_server = os.environ.get("KAFKA_TARGET_BOOTSTRAP_SERVERS","localhost:9092").split(",")
kafka_tgt_topic = os.environ.get('KAFKA_TARGET_TOPIC','t_topic2')
proc_name = os.environ.get('MODULE_NAME','GENERIC_MODULE')

print("Environment variables:")
print(f"KAFKA_SOURCE_BOOTSTRAP_SERVERS = {kafka_src_server}")
print(f"KAFKA_SOURCE_TOPIC = {kafka_src_topic}")
print(f"KAFKA_TARGET_BOOTSTRAP_SERVERS = {kafka_tgt_server}")
print(f"KAFKA_TARGET_TOPIC = {kafka_tgt_topic}")
print(f"MODULE_NAME = {proc_name}")

#--------------- Template Code, Avoid changing anything in this section --------------------------# 
class AbstractKafkaInStreamProcessor(ABC):
        
    def produce_data_kafka(self,record) -> None:
      self.producer.send(topic=kafka_tgt_topic, value=record)


    @abstractmethod
    def init_hook(self) -> None:
        return null



    @abstractmethod
    def process_data(self,record) -> None:        
        return record



    def kafka_in_stream_processor(self) -> None:

        for message in self.consumer:            
            #try:
                self.processed_record = self.process_data(message)
                self.produce_data_kafka(self.processed_record)
            #except:
            #    print("Skipping Record..")


    def __init__(self):

        print("Initializing Kafka Consumer")        
        self.consumer = KafkaConsumer(kafka_src_topic, group_id = proc_name, bootstrap_servers = kafka_src_server,value_deserializer=lambda m: json.loads(m.decode('utf-8')))

        print("Initializing Kafka Producer") 
        self.producer = KafkaProducer(bootstrap_servers = kafka_tgt_server, value_serializer = lambda v: json.dumps(v).encode('utf-8'))





def run(abstract_class: AbstractKafkaInStreamProcessor) -> None:
    """
    The client code calls the template method to execute the algorithm. Client
    code does not have to know the concrete class of an object it works with, as
    long as it works with objects through the interface of their base class.
    """

    # ...
    abstract_class.kafka_in_stream_processor()
    # ...


#-------------------------Template Code Ends Here ------------------------------------#




class ConKafkaInStreamProcessor(AbstractKafkaInStreamProcessor):

    def init_hook(self):
        self.new_list

    
    
    def process_data(self,message) -> None:
#------------------- Add module Logic in this section ---------------------#
        #try:
            #-- Perform all the module logic here --#

            # To get value from a field (Example)z
            json_util = util.JsonDataUtil(message.value)
            

            tweet_text = json_util.get_value("text")

            json_util.retain_fields(["created_at","id","text","user","place"])
            #Do Processing

            #Adding metadata to the record (Example)
        
            json_util.add_metadata("lews_meta_test",'{"Test1": 34.3434, "Test2": 42.534}')
            #util.json_util.add_metadata("Longitude","-1.617780")

        #except Exception as ex:
        #    print("Invalid Tweet Record.. Skipping", ex)
        #    raise

        #Get the processed record with metadata added
            processes_message = json_util.get_json()
            print("Processing done, Attaching sample metadata")
#---------------------- Add module logic in this section (End) ----------------------#
            return processes_message



if __name__ == "__main__":
   run(ConKafkaInStreamProcessor())
