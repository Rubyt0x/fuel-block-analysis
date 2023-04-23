extern crate alloc;
use fuel_indexer_macros::indexer;
use fuel_indexer_plugin::prelude::*;

#[indexer(manifest = "hello_indexer.manifest.yaml")]
pub mod hello_indexer_index_mod {

    fn hello_indexer_handler(block_data: BlockData) {
        Logger::info("Processing a block. (>'.')>");

        let block_id = first8_bytes_to_u64(block_data.id);
        let block = Block{ id: block_id, height: block_data.height, hash: block_data.id };
        block.save();

        for transaction in block_data.transactions.iter() {
            Logger::info("Handling a transaction (>'.')>");

            let tx = Tx{ id: first8_bytes_to_u64(transaction.id), block: block_id, hash: transaction.id };
            tx.save();
        }
    }
}
