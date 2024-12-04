from fairseq.models import register_model_architecture
from fairseq.models.transformer import base_architecture

@register_model_architecture("transformer", "transformer_24_24")
def transformer_xdeep(args):
    args.encoder_embed_dim = getattr(args, "encoder_embed_dim", 1024)
    args.encoder_ffn_embed_dim = getattr(args, "encoder_ffn_embed_dim", 8 * 1024)
    args.encoder_attention_heads = getattr(args, "encoder_attention_heads", 16)
    args.encoder_normalize_before = getattr(args, "encoder_normalize_before", True)
    args.decoder_normalize_before = getattr(args, "decoder_normalize_before", True)
    args.decoder_embed_dim = getattr(args, "decoder_embed_dim", 1024)
    args.decoder_ffn_embed_dim = getattr(args, "decoder_ffn_embed_dim", 8 * 1024)
    args.decoder_attention_heads = getattr(args, "decoder_attention_heads", 16)
    args.encoder_layers = getattr(args, "encoder_layers", 18)
    args.decoder_layers = getattr(args, "decoder_layers", 18)
    base_architecture(args)
