from abc import ABC, abstractmethod
from kafka import KafkaConsumer, KafkaProducer
import json
import os


#--------------- Template Code, Avoid changing anything in this section --------------------------# 
class AbstractKafkaInStreamProcessor(ABC):
        
    def produce_data_kafka(self,record) -> None:
      
      self.producer.send(topic=self.target_topic,value=record)
      #print("Processed Record Sent")



    @abstractmethod
    def process_data(self,record) -> None:
        
        return record



    def kafka_in_stream_processor(self) -> None:

        for message in self.consumer:
        
            self.processed_record = self.process_data(message)
        
            self.produce_data_kafka(self.processed_record)




    def __init__(self,processor_name,source_topic,target_topic):

        self.processor_name = processor_name
        
        self.source_topic = source_topic
        
        self.target_topic = target_topic
        
        self.bootstrap_servers = os.getenv('KAFKA_BROKER','host.docker.internal:9092')
        #self.bootstrap_servers = 'localhost:9092'
        
        print("Initializing Kafka In-Stream Processor Module")
        
        self.consumer = KafkaConsumer(source_topic,group_id = self.processor_name, bootstrap_servers = self.bootstrap_servers,value_deserializer=lambda m: json.loads(m.decode('utf-8')))

       # self.producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers)

        self.producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers, value_serializer = lambda v: json.dumps(v).encode('utf-8'))




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

     def process_data(self,message) -> None:

        #Do Processing
#-- Perform all the module logic here --#
        #Return processed json string
        processes_message = message.value

        return processes_message



if __name__ == "__main__":

    #processor_name: Unique processor name for the module, 
    #source_topic: Topic from which the module should accept the record to be processed, 
    # target_topic: Topic to which the module publishes the processed record
   s_topic = os.getenv('MODULE_SRC_TOPIC','lews-twitter')
   t_topic = os.getenv('MODULE_TGT_TOPIC','t_topic')
   proc_name = os.getenv('MODULE_NAME','Module01')  
   
   run(ConKafkaInStreamProcessor(processor_name=proc_name, source_topic=s_topic, target_topic=t_topic))
