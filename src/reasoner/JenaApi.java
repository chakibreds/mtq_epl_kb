import java.io.InputStream;

import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.InfModel;
import org.apache.jena.reasoner.Reasoner;
import org.apache.jena.reasoner.ReasonerRegistry;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.util.FileManager;

public class JenaApi {
    public Model read(String file_name) throws Exception {
        if (file_name == null) {
            throw new Exception("Please specify the path of an RDF/XML file");
        } else {
            Model model = ModelFactory.createDefaultModel();

            InputStream in = FileManager.get().open(file_name);
            if (in == null) {
                throw new Exception("Can't read file '"+file_name+"'");
            } else {
                model.read(in, null);
            }

            return model;
        }
    }
    public InfModel inference(Model schema, Model model) {
        Reasoner reasoner = ReasonerRegistry.getOWLReasoner();
        reasoner = reasoner.bindSchema(schema);
        return ModelFactory.createInfModel(reasoner, model);
    }
    public static void main(String[] args) {
        String data_file, schema_file;
        if (args.length == 2) {
            schema_file = args[0];
            data_file = args[1];
        } else {
            System.err.println("Veuillez donnez les noms des fichiers");
            return ;
        }

        JenaApi jena = new JenaApi();
        // Model schema = ModelFactory.createDefaultModel(); // model vide
        Model data = ModelFactory.createDefaultModel(); // model vide
        Model schema = ModelFactory.createDefaultModel(); // model vide
        
        try {
            data = jena.read(data_file);
            schema = jena.read(schema_file);

        } catch (Exception e) {
            System.err.println("Exc: " + e);
        }

        InfModel inf = jena.inference(schema, data);

        // Affichage du model sur la sortie standard
        inf.write(System.out); // en RDF/XML
    }
}

