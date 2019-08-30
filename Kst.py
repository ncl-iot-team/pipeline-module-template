from abc import ABC, abstractmethod

class AbstractKafkaInStreamProcessor(ABC):

    def consume_data_kafka(self) -> None:
        print("Consume a record from Kafka")

    def produce_data_kafka(self) -> None:
        print("Publish a record to Kafka")
    
    @abstractmethod
    def process_data(self) -> None:
        pass

    
    def kafka_in_stream_processor(self) -> None:
        self.consume_data_kafka()

        self.process_data()

        self.produce_data_kafka()
    

def client_code(abstract_class: AbstractKafkaInStreamProcessor) -> None:
    """
    The client code calls the template method to execute the algorithm. Client
    code does not have to know the concrete class of an object it works with, as
    long as it works with objects through the interface of their base class.
    """

    # ...
    abstract_class.kafka_in_stream_processor()
    # ...


if __name__ == "__main__":
    client_code(ConKafkaInStreamProcessor())